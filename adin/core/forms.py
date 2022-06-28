from django.forms import ModelForm, ValidationError

class GenericCreateForm(ModelForm):

    pk_name = None

    def save(self, *args, **kwargs):
        base_args = {k: self.cleaned_data[k] for k in self.fields}
        base_args['state_change_user'] = self.creator
        obj = self._meta.model(**base_args)
        obj.save()
        return obj

    def set_readonly_fields(self, fields=[]):
        for field in self.fields:
            if field in fields:
                self.fields[field].widget.attrs['readonly'] = True
            else: 
                self.fields[field].widget.attrs['readonly'] = False

    def clean_pk(self):
        data = self.cleaned_data.get(self.pk_name)
        if self._meta.model.objects.filter(pk=data).exists():
            obj = self._meta.model.objects.get(pk=data)
            if obj.state == 0:
                raise ValidationError(f"{self._meta.model._meta.verbose_name} con {self._meta.model._meta.get_field(self.pk_name).verbose_name} ya existe y está inactiva.")
            else:
                raise ValidationError(f"{self._meta.model._meta.verbose_name} con {self._meta.model._meta.get_field(self.pk_name).verbose_name} ya existe.")
        return data

class GenericUpdateForm(ModelForm):
    
    readonly_fields = []

    def clean(self):
        for field in self.changed_data:
            if field in self.readonly_fields:
                self.add_error(None, f'Hubo cambios en los datos inmutables del objeto.')
        return super().clean()

    def set_readonly_fields(self, fields=[]):
        for field in self.fields:
            if field in fields:
                self.readonly_fields.append(field)
                self.fields[field].widget.attrs['readonly'] = True
            else: 
                self.fields[field].widget.attrs['readonly'] = False

class GenericDeleteForm(ModelForm):

    exclude_fields = []

    def clean(self):
        objs = []
        for field in self.instance._meta._get_fields(forward=False, reverse=True, include_hidden=True):
            if field.related_name: 
                for obj in eval(f'self.instance.{field.related_name}.all()'):
                    if field.many_to_many:
                        thr_obj = field.through.find.from_related(self.instance, obj)
                        if thr_obj.state != 0:
                            objs.append(thr_obj)
                    elif field.name not in self.exclude_fields:
                        if obj.state != 0:
                            objs.append(obj)
                        
        if len(objs) > 0:
            msg = f'{self.instance._meta.verbose_name} no se puede inactivar ya que tiene relación con los siguientes objetos: {objs}'
            self.add_error(None, msg)

        if self.has_changed(): 
            raise ValidationError(f'Hubo cambios en los datos inmutables del objeto.')
        return super().clean()

class GenericActivateForm(ModelForm):

    def clean(self):
        if self.has_changed():
            self.add_error(None, f'Hubo cambios en los datos inmutables del objeto.')
        return super().clean()

class GeneriCreateRelatedForm(GenericCreateForm):

    related_fields = []

    def clean(self):
        base_fields = {}
        for field in self.fields:
            self.cleaned_data[field]
            if field in self.related_fields:
                base_fields[field] = self.cleaned_data.get(field)
        if self._meta.model.objects.filter(**base_fields).exists():
            obj = self._meta.model.objects.get(**base_fields)
            if obj.state == 0:
                raise ValidationError(f"{self._meta.model._meta.verbose_name} con estos valores ya existe y está inactiva.")
            else:
                raise ValidationError(f"{self._meta.model._meta.verbose_name} con estos valores ya existe.")
        return super().clean()
    
class GenericUpdateRelatedForm(GenericUpdateForm):

    def save(self, *args, **kwargs):
        get_args = {}
        update_args = {}
        for k in self.fields:
            if k in args[0]:
                get_args[k] = self.cleaned_data[k]
            elif k in self.changed_data:
                update_args[k] = self.cleaned_data[k]
        obj = self._meta.model.objects.get(**get_args)
        for k, v in update_args.items():
            setattr(obj, k, v)
        obj.state_change_user = self.creator
        obj.save()
    
class GenericDeleteRelatedForm(ModelForm):

    def clean(self):
        if self.has_changed():
            self.add_error(None, f'Hubo cambios en los datos inmutables del objeto.')
        return super().clean()

class GenericActivateRelatedForm(ModelForm):

    related_fields = []

    def clean(self):
        objs = []
        for field in self.instance._meta._get_fields(forward=True, reverse=False):
            if field.is_relation:
                if field.name in self.related_fields:
                    obj = eval(f'self.instance.{field.name}')
                    if obj.state == 0:
                        objs.append(obj)
        if len(objs) > 0:
            msg = f'{self.instance._meta.verbose_name} no se puede activar ya que los siguientes objetos están inactivos: {objs}'
            self.add_error(None, msg)
        return super().clean()
