from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

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
