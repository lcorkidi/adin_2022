from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

class GenericDetailView(LoginRequiredMixin, View):

    template = 'adin/generic_detail.html'
    title = None
    subtitle = 'Ver'
    model = None
    form = None
    ref_urls = None
    choice_fields = None
    m2m_data = None
    actions_off = None

    def get(self, request, pk):
        obj = self.model.objects.get(pk=pk)
        form = self.form(instance=obj)
        if self.m2m_data:
            m2m_data = self.m2m_data()
            for attr, data in m2m_data.items():
                filter_expresion = {}
                filter_expresion[data['filter_expresion']] = pk
                formset = data['formset'](queryset=data['class'].objects.exclude(state=0).filter(person__id_number=pk))
                m2m_data[attr]['formset'] = formset
        else:
            m2m_data = None
        context = {'title':self.title, 'subtitle':self.subtitle, 'ref_urls':self.ref_urls, 'form':form, 'm2m_data':m2m_data, 'choice_fields':self.choice_fields, 'actions_off': self.actions_off }
        return render(request, self.template, context)

class GenerricCreateView(LoginRequiredMixin, View):

    template = 'adin/generic_create.html'
    form = None
    title = None
    subtitle = 'Crear'
    ref_urls = None
    
    def get(self, request):
        form = self.form()
        context = {'form': form, 'title': self.title, 'subtitle': self.subtitle, 'ref_urls': self.ref_urls}
        return render(request, self.template, context)

    def post(self, request):
        form = self.form(request.POST)
        if not form.is_valid():
            context = {'form': form, 'title': self.title, 'subtitle': self.subtitle, 'ref_urls': self.ref_urls}
            return render(request, self.template, context)
        form.creator = request.user
        per = form.save()            
        return redirect(self.ref_urls['list'])

class GenericUpdateView(LoginRequiredMixin, View):

    template = 'people/people_update.html'
    model = None
    form = None
    title = None
    subtitle = 'Actualizar'
    ref_urls = None
    readonly_fields = None
    choice_fields = None
    m2m_data = None

    def get(self, request, pk):
        obj = self.model.objects.get(pk=pk)
        form = self.form(instance=obj)
        if self.readonly_fields:
            form.set_readonly_fields(self.readonly_fields)
        if self.m2m_data:
            m2m_data = self.m2m_data()
            for attr, data in m2m_data.items():
                form.set_hidden_field(attr)
                filter_expresion = {}
                filter_expresion[data['filter_expresion']] = pk
                formset = data['formset'](queryset=data['class'].objects.exclude(state=0).filter(**filter_expresion))
                m2m_data[attr]['formset'] = formset
        else:
            m2m_data = None
        context = {'form': form, 'title': self.title, 'subtitle': self.subtitle, 'ref_urls': self.ref_urls, 'choice_fields': self.choice_fields, 'm2m_data': m2m_data}
        return render(request, self.template, context)

    def post(self, request, pk):
        obj = self.model.objects.get(pk=pk)
        form = self.form(request.POST, instance=obj)
        if not form.is_valid():
            if self.readonly_fields:
                form.set_readonly_fields(self.readonly_fields)
            if self.m2m_data:
                m2m_data = self.m2m_data()
                for attr, data in m2m_data.items():
                    form.set_hidden_field(attr)
                    filter_expresion = {}
                    filter_expresion[data['filter_expresion']] = pk
                    formset = data['formset'](queryset=data['class'].objects.exclude(state=0).filter(**filter_expresion))
                    m2m_data[attr]['formset'] = formset
            else:
                m2m_data = None
            context = {'form': form, 'title': self.title, 'subtitle': self.subtitle, 'ref_urls': self.ref_urls, 'choice_fields': self.choice_fields, 'm2m_data': m2m_data}
            return render(request, self.template, context)
        form.save()
        return redirect(self.ref_urls['list'])


class GenericDeleteView(LoginRequiredMixin, View):

    template = 'adin/generic_delete.html'
    title = None
    subtitle = 'Inactivar'
    model = None
    form = None
    ref_urls = None
    choice_fields = None
    m2m_data = None
    actions_off = None

    def get(self, request, pk):
        obj = self.model.objects.get(pk=pk)
        form = self.form(instance=obj)
        if self.m2m_data:
            m2m_data = self.m2m_data()
            for attr, data in m2m_data.items():
                form.set_hidden_field(attr)
                filter_expresion = {}
                filter_expresion[data['filter_expresion']] = pk
                formset = data['formset'](queryset=data['class'].objects.exclude(state=0).filter(person__id_number=pk))
                m2m_data[attr]['formset'] = formset
        else:
            m2m_data = None
        context = {'title':self.title, 'subtitle':self.subtitle, 'ref_urls':self.ref_urls, 'form':form, 'm2m_data':m2m_data, 'choice_fields':self.choice_fields, 'actions_off': self.actions_off }
        return render(request, self.template, context)

    def post(self, request, pk):
        obj = self.model.objects.get(pk=pk)
        form = self.form(request.POST, instance=obj)
        m2m_data = self.m2m_data()
        if form.has_changed():
            if self.m2m_data:
                for attr, data in m2m_data.items():
                    form.set_hidden_field(attr)
                    formset = data['formset'](queryset=data['class'].objects.exclude(state=0).filter(person__id_number=pk))
                    m2m_data[attr]['formset'] = formset
                context = {'title':self.title, 'subtitle':self.subtitle, 'ref_urls':self.ref_urls, 'form':form, 'm2m_data':m2m_data, 'choice_fields':self.choice_fields, 'actions_off': self.actions_off }
                return render(request, self.template, context)
            else:
                m2m_data = None
        for attr, data in m2m_data.items():
            data['class'].objects.exclude(state=0).filter(person__id_number=pk).update(state=0)
        obj.state = 0
        obj.save()
        return redirect(self.ref_urls['list'])

class GenericCreateRelatedView(LoginRequiredMixin, View):

    template = None
    form = None
    title = None
    subtitle = 'Crear'
    ref_urls = None
    readonly_fields = None

    def get(self, request, pk):
        form = self.form({self.readonly_fields[0]:pk})
        form.set_readonly_fields(self.readonly_fields)
        context = {'title':self.title, 'subtitle':self.subtitle, 'ref_urls': self.ref_urls, 'form':form, 'errors':False, 'ref_pk':pk}
        return render(request, self.template, context)

    def post(self, request, pk):
        form = self.form(request.POST)
        if not form.is_valid():
            form.set_readonly_fields(self.readonly_fields)
            context = {'title':self.title, 'subtitle':self.subtitle, 'ref_urls': self.ref_urls, 'form':form, 'errors':False, 'ref_pk':pk}
            return render(request, self.template, context)
        form.creator = request.user
        form.save()            
        return redirect(self.ref_urls['update'], pk)

class GenericUpdateRelatedView(LoginRequiredMixin, View):

    template = None
    model = None
    form = None
    title = None
    subtitle = 'Actualizar'
    ref_urls = None
    rel_urls = None
    readonly_fields = None

    def get(self, request, ret_pk, pk):
        obj = self.model.objects.get(pk=pk)
        form = self.form(instance=obj)
        form.set_readonly_fields(self.readonly_fields)
        context = {'title':self.title, 'subtitle':self.subtitle, 'ref_urls': self.ref_urls, 'rel_urls':self.rel_urls, 'form':form, 'errors':False, 'ref_pk':ret_pk}
        return render(request, self.template, context)

    def post(self, request, ret_pk, pk):
        obj = self.model.objects.get(pk=pk)
        form = self.form(request.POST, instance=obj)
        if not form.is_valid():
            form.set_readonly_fields(self.readonly_fields)
            context = {'title':self.title, 'subtitle':self.subtitle, 'ref_urls': self.ref_urls, 'rel_urls':self.rel_urls, 'form':form, 'errors':False, 'ref_pk':ret_pk}
            return render(request, self.template, context)
        form.creator = request.user
        form.save(self.readonly_fields)           
        return redirect(self.ref_urls['update'], ret_pk)

class GenericDeleteRelatedView(LoginRequiredMixin, View):

    template = None
    model = None
    title = None
    subtitle = 'Inactivar'
    form = None
    ref_urls = None
    rel_urls = None
    choice_fields = None
    
    def get(self, request, ret_pk, pk):
        obj = self.model.objects.get(pk=pk)
        form = self.form(instance=obj)
        context = {'title':self.title, 'subtitle':self.subtitle, 'ref_urls':self.ref_urls, 'rel_urls':self.rel_urls, 'form':form, 'ref_pk': ret_pk, 'choice_fields':self.choice_fields}
        return render(request, self.template, context)

    def post(self, request, ret_pk, pk):
        obj = self.model.objects.get(pk=pk)
        obj.state = 0
        obj.save()
        return redirect(self.ref_urls['update'], ret_pk)
