from django.forms import ModelForm, ValidationError

class GenericCreateForm(ModelForm):

    pk_name = None

    def save(self, *args, **kwargs):
        base_args = {k: self.cleaned_data[k] for k in self.fields}
        base_args['state_change_user'] = self.creator
        per_nat = self._meta.model(**base_args)
        per_nat.save()
        return per_nat

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

    def set_readonly_fields(self, fields=[]):
        for field in self.fields:
            if field in fields:
                self.readonly_fields.append(field)
                self.fields[field].widget.attrs['readonly'] = True
            else: 
                self.fields[field].widget.attrs['readonly'] = False

class GenericDeleteForm(ModelForm):

    def clean(self):
        objs = []
        for obj in self.instance._meta._get_fields(forward=False, reverse=True, include_hidden=True):
            if (not obj.hidden or obj.field.many_to_many) and obj.related_name: 
                for obj in eval(f'self.instance.{obj.related_name}.all()'):
                    objs.append(obj)
        if len(objs) > 0:
            msg = f'Direccion no se puede inactivar ya que tiene relación con los siguientes objetos: {objs}'
            self.add_error(None, msg)

        if self.has_changed(): 
            raise ValidationError(None, f'Hubo cambios en los datos inmutables del objeto.')

class GeneriCreateRelatedForm(GenericCreateForm):
    # validate unique constraint value objects is active and raise error if so
    pass

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
        obj.state_change_date = self.creator
        obj.save()
