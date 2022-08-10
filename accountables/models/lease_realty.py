import datetime
import pandas as pd
from django.db import models
from dateutil.relativedelta import relativedelta

from adin.core.models import BaseModel
from .accountable import Accountable
from .date_value import Date_Value
from accountables.utils import lease_realty_code
from adin.utils.date_progression import nextmonthlydate, nextyearlydate, previousmonthlydate, previousyearlydate
from adin.utils.data_check import children_errors_report

class Lease_Realty(Accountable):

    realty = models.ManyToManyField(
        'properties.Realty', 
        through='Lease_Realty_Realty', 
        through_fields=('lease', 'realty'),
        related_name='leases_realties',
        related_query_name='lease_realty',
        verbose_name='Inmueble'
    )
    part = models.ManyToManyField(
        'people.Person', 
        through='Lease_Realty_Person', 
        through_fields=('lease', 'person'),
        related_name='leases_realties',
        related_query_name='lease_realty',
        verbose_name='Parte'
    )
    doc_date = models.DateField(
        verbose_name='Fecha Contrato'
    )
    start_date = models.DateField(
        null=True,
        blank=True,
        default=None,
        verbose_name='Fecha Ocupación'
    )
    end_date = models.DateField(
        null=True,
        blank=True,
        default=None,
        verbose_name='Fecha Desocupación'
    )   
    
    class Meta:
        app_label = 'accountables'
        verbose_name = 'Arriendo Inmueble'
        verbose_name_plural = 'Arriendos Inuembles'
        permissions = [
            ('activate_lease_realty', 'Can activate lease realty.'),
        ]

    @classmethod
    def get_errors_report(cls, all=False):
        return children_errors_report(cls, all)

    @classmethod
    def check_doc_date_availability(cls, realties, doc_date):
        for lease in cls.objects.filter(realty__in=realties).distinct():
            if lease.check_date_intersection(doc_date):
                return False
        return True

    def check_date_intersection(self, doc_date):
        if not self.start_date:
            return False
        date_range = pd.date_range(self.start_date, self.end_date if self.end_date else datetime.date.today())
        if doc_date in date_range:
            return True
        return False

    def is_active(self):
        if self.start_date and not self.end_date:
            return True
        return False

    def ledger_holder(self):
        return self.lease_realty_person_set.get(lease=self, role=3).person

    def ledger_third_party(self):
        return self.lease_realty_person_set.get(lease=self, role=1).person

    def pending_accountable_concept_dates(self, first_concept_date=None):
        date_list = self.date_list(first_concept_date) if first_concept_date else self.date_list(self.accountable_concept.latest('date') if self.accountable_concept.exists() else None)
        for date in self.accountable_concept.filter(state=0).values_list('date', flat=True):
            if date in date_list:
                date_list.remove(date)
        return date_list

    def pending_date_value_dates(self, first_concept_date=None):
        date_values = [item['date'] for item in self.date_value.exclude(state=0).values('date')]
        dates = []
        if first_concept_date:
            ref_date = previousyearlydate(self.doc_date, first_concept_date)
        else:
            ref_date = self.doc_date
        while ref_date <= datetime.date.today() + relativedelta(months=+3):
            if ref_date not in date_values:
                dates.append(ref_date)
            ref_date = nextyearlydate(self.doc_date, ref_date)
        return dates

    def pending_date_values(self):
        date_values = Date_Value.objects.filter(accountable=self)
        today = datetime.date.today()
        if self.end_date and self.end_date < today:
            end_date = self.end_date
        else:
            end_date = today
        years = relativedelta(previousmonthlydate(self.doc_date, end_date), self.doc_date).years
        dates = []
        ref_date = self.doc_date
        dates.append(ref_date)
        for year in range(years):
            ref_date = nextyearlydate(self.doc_date, ref_date)
            dates.append(ref_date)
        for date_value in date_values:
            if date_value.date in dates:
                dates.remove(date_value.date)
        return dates

    def date_list(self, start_date=None):
        if start_date:
            self.start_date = start_date
        date_list = []
        today = datetime.date.today()
        if self.start_date and self.start_date < today:
            ref_date = self.start_date
            if self.end_date and self.end_date < today:
                end_date = self.end_date
            else:
                end_date = today
            delta = relativedelta(previousmonthlydate(self.doc_date, end_date), self.start_date)
            abs_delta_months = (delta.years * 12) + delta.months + 1 if delta.days == 0 else (delta.years * 12) + delta.months + 2
            for i in range(abs_delta_months):
                date_list.append(ref_date)
                ref_date = nextmonthlydate(self.doc_date, ref_date)
        return date_list

    def date_value_dict(self):
        date_list = self.date_list()
        date_value_dict = {}
        date_vals = Date_Value.objects.filter(accountable=self).order_by('date')
        date_val, index = date_vals[0], 0
        for date in date_list:
            if index < date_vals.count() - 1:
                if date >= date_vals[index + 1].ref_date:
                    date_val, index = date_vals[index + 1], index + 1
            if not self.end_date or self.end_date >= nextmonthlydate(self.doc_date, date):
                date_value_dict[date] = round(((nextmonthlydate(self.doc_date, date) - date).days / (nextmonthlydate(self.doc_date, date) - previousmonthlydate(self.doc_date, date)).days) * int(date_val.value), 0)
            else:
                date_value_dict[date] = round(((self.end_date - previousmonthlydate(self.doc_date, date)).days / (nextmonthlydate(self.doc_date, date) - previousmonthlydate(self.doc_date, date)).days) * int(date_val.value), 0)
        return date_value_dict

    def get_obj_errors(self):
        errors = []
        # realty (primary count 1 active)
        if not self.lease_realty_realty_set.exclude(state=0).filter(primary=True).exists():
            errors.append(130)
        else:
            if self.lease_realty_realty_set.exclude(state=0).filter(primary=True).count() > 1:
                errors.append(131)
            elif self.lease_realty_realty_set.exclude(state=0).filter(realty__state=0).exists():
                errors.append(132)
        # part (role 0 active, role 1 active > 1, role 2 active > 1, role 3 active > 1, active role 0, 1 and 2 active address)
        if self.lease_realty_person_set.exclude(state=0).filter(role=0, person__state=0).exists():
            errors.append(134)
        if not self.lease_realty_person_set.exclude(state=0).filter(role=1).exists():
            errors.append(135)
        elif self.lease_realty_person_set.exclude(state=0).filter(role=1, person__state=0).exists():
            errors.append(136)
        if not self.lease_realty_person_set.exclude(state=0).filter(role=2).exists():
            errors.append(137)
        elif self.lease_realty_person_set.exclude(state=0).filter(role=2, person__state=0).exists():
            errors.append(138)
        if not self.lease_realty_person_set.exclude(state=0).filter(role=3).exists():
            errors.append(139)
        else:
            if self.lease_realty_person_set.exclude(state=0).filter(role=3).count() > 1:
                errors.append(133) 
            if self.lease_realty_person_set.exclude(state=0).filter(role=3, person__state=0).exists():
                errors.append(140)
        if self.lease_realty_person_set.exclude(state=0).filter(role__in=[0, 1, 2], address=None).exists():
            errors.append(141)
        # doc_date (obligatory, date, vacant)
        if not self.doc_date:
            errors.append(142)
        else:
            if not isinstance(self.doc_date, datetime.date):
                errors.append(143)
            elif self.realty and not Lease_Realty.check_doc_date_availability(self.realty.all(), self.doc_date):
                errors.append(144)
        # start_date (date, vacant)
        if self.start_date and not isinstance(self.start_date, datetime.date):
            errors.append(145)
        elif self.realty and not Lease_Realty.check_doc_date_availability(self.realty.all(), self.start_date):
            errors.append(146)
        # end_date (if start_date, < start_date, date)
        if self.end_date and not isinstance(self.end_date, datetime.date):
            errors.append(147)
        elif self.end_date:
            if not self.start_date:
                errors.append(148)
            elif self.end_date < self.start_date:
                errors.append(149)
        # code (obligatory, from function)
        if not self.code:
            errors.append(150)
        elif self.lease_realty_realty_set.exclude(state=0).filter(primary=True).count() == 1 and self.doc_date and self.code != lease_realty_code(self.lease_realty_realty_set.exclude(state=0).get(primary=True).realty, self.doc_date):
            errors.append(151)
        # subclass (obligatory, = contenttype id)
        if not self.subclass:
            errors.append(152)
        elif self.subclass != self._meta.get_field('subclass').remote_field.model.objects.get(model=self._meta.model.__name__.lower()):
            errors.append(153)
        # transaction_types (active)
        if self.transaction_types.filter(state=0).exists():
            errors.append(154)
        return errors

    def __repr__(self) -> str:
        return f'<Lease_Realty: {self.code}>'
    
    def __str__(self) -> str:
        return f'{self.lease_realty_realty_set.get(primary=True).realty if self.lease_realty_realty_set.filter(primary=True).exists() and self.lease_realty_person_set.filter(role=1).count()==1 else "None"}^{self.lease_realty_person_set.get(role=1).person if self.lease_realty_person_set.filter(role=1).exists() and self.lease_realty_person_set.filter(role=1).count()==1 else "None"}'

class Lease_Realty_RealtyFinderManager(models.Manager):
    def from_related(self, obj1, obj2):
        base_args = {}
        if isinstance(obj1, Lease_Realty):
            base_args['lease'] = obj1
            base_args['realty'] = obj2
        else:
            base_args['lease'] = obj2
            base_args['realty'] = obj1
        return self.get_queryset().get(**base_args)

    def get_queryset(self):
        return super().get_queryset()

class Lease_Realty_Realty(BaseModel):

    lease = models.ForeignKey(
        Lease_Realty,
        on_delete=models.PROTECT,
        verbose_name='Contrato'
    )
    realty = models.ForeignKey(
        'properties.Realty',
        on_delete=models.PROTECT,
        verbose_name='Inmueble'
    )
    primary = models.BooleanField(
        verbose_name='Primario'
    )

    objects = models.Manager()
    find = Lease_Realty_RealtyFinderManager()
 
    class Meta:
        app_label = 'accountables'
        verbose_name = 'Inmueble Arriendo Inmueble'
        verbose_name_plural = 'Inmuebles Arriendos Inmuebles'

    def __repr__(self) -> str:
        return f'<Lease_Realty_Realty: {self.lease.pk}_{self.realty.pk}>'
    
    def __str__(self) -> str:
        return f'{self.lease.pk}_{self.realty.pk}'

class Lease_Realty_PersonFinderManager(models.Manager):
    def from_related(self, obj1, obj2):
        base_args = {}
        if isinstance(obj1, Lease_Realty):
            base_args['lease'] = obj1
            base_args['person'] = obj2
        else:
            base_args['lease'] = obj2
            base_args['person'] = obj1
        return self.get_queryset().get(**base_args)

    def get_queryset(self):
        return super().get_queryset()

class Lease_Realty_Person(BaseModel):

    ROLE_CHOICE = [
        (0,'Arrendador'),
        (1,'Arrendatario'),
        (2,'Fiador'),
        (3,'Arrendador Titular')
    ]
    
    lease = models.ForeignKey(
        Lease_Realty,
        on_delete=models.PROTECT,
        verbose_name='Contrato'
    )
    person = models.ForeignKey(
        'people.Person',
        on_delete=models.PROTECT,
        verbose_name='Persona'
    )
    role = models.PositiveSmallIntegerField(
        choices=ROLE_CHOICE,
        verbose_name='Rol'
    )
    phone = models.ForeignKey(
        'references.Phone',
        on_delete=models.PROTECT,
        related_name='leases_realties_people',
        related_query_name='lease_realty_person',
        null=True,
        blank=True,
        default=None,
        verbose_name='Teléfono'
    )
    e_mail = models.ForeignKey(
        'references.E_Mail',
        on_delete=models.PROTECT,
        related_name='leases_realties_people',
        related_query_name='lease_realty_person',
        null=True,
        blank=True,
        default=None,
        verbose_name='Correo Electrónico',
    )
    address = models.ForeignKey(
        'references.Address',
        on_delete=models.PROTECT,
        related_name='leases_realties_people',
        related_query_name='lease_realty_person',
        verbose_name='Dirección'
    )

    objects = models.Manager()
    find = Lease_Realty_PersonFinderManager()
 
    class Meta:
        app_label = 'accountables'
        verbose_name = 'Parte Arriendo Inmueble'
        verbose_name_plural = 'Partes Arriendos Inmuebles'

    def __repr__(self) -> str:
        return f'<Lease_Realty_Person: {self.lease.pk}_{self.person.complete_name}>'
    
    def __str__(self) -> str:
        return f'{self.lease.pk}_{self.person.complete_name}'
