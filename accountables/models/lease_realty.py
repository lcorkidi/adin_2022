import datetime
from django.db import models
from dateutil.relativedelta import relativedelta

from adin.core.models import BaseModel
from .accountable import Accountable
from .date_value import Date_Value
from adin.utils.date_progression import nextmonthlydate, nextyearlydate, previousmonthlydate


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
        verbose_name='Fecha Ocupacion'
    )
    end_date = models.DateField(
        null=True,
        blank=True,
        default=None,
        verbose_name='Fecha Desocupacion'
    )
    
    class Meta:
        app_label = 'accountables'
        verbose_name = 'Arriendo Inmueble'
        verbose_name_plural = 'Arriendos Inuembles'
        permissions = [
            ('activate_lease_realty', 'Can activate lease realty.'),
        ]

    def is_active(self):
        if self.start_date and not self.end_date:
            return True
        return False

    def accounting_holder(self):
        from people.models import Person
        return Person.objects.get(pk=6108014)

    def accounting_third_party(self):
        return self.leases_realties_people.all().filter(role=1)[0].person

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

    def date_list(self):
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
        if self.pending_date_values():
            raise Warning('Pending "Date_Value":', self.pending_date_values())
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

    def __repr__(self) -> str:
        return f'<Lease_Realty: {self.code}>'
    
    def __str__(self) -> str:
        return self.code

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
 
    class Meta:
        app_label = 'accountables'
        verbose_name = 'Inmueble Arriendo Inmueble'
        verbose_name_plural = 'Inmuebles Arriendos Inmuebles'

    def __repr__(self) -> str:
        return f'<Lease_Realty_Person: {self.lease.pk}_{self.realty.pk}>'
    
    def __str__(self) -> str:
        return f'{self.lease.pk}_{self.realty.pk}'

class Lease_Realty_Person(BaseModel):

    ROLE_CHOICE = [
        (0,'Arrendador'),
        (1,'Arrendatario'),
        (2,'Fiador')
    ]
    
    lease = models.ForeignKey(
        Lease_Realty,
        on_delete=models.PROTECT,
        related_name='leases_realties_people',
        related_query_name='lease_realty_person',
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
        null=True,
        blank=True,
        default=None,
        verbose_name='Teléfono'
    )
    e_mail = models.ForeignKey(
        'references.E_Mail',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        default=None,
        verbose_name='Correo Electrónico',
    )
    address = models.ForeignKey(
        'references.Address',
        on_delete=models.PROTECT,
        verbose_name='Dirección'
    )
 
    class Meta:
        app_label = 'accountables'
        verbose_name = 'Parte Arriendo Inmueble'
        verbose_name_plural = 'Partes Arriendos Inmuebles'

    def __repr__(self) -> str:
        return f'<Lease_Realty_Person: {self.lease.pk}_{self.person.complete_name}>'
    
    def __str__(self) -> str:
        return f'{self.lease.pk}_{self.person.complete_name}'
