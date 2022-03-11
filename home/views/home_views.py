from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import View

class HomeView(LoginRequiredMixin, View):

    template = 'home/user_home.html'
    title = 'Inicio'

    def get(self, request):
        context = {'title': self.title}
        return render(request, self.template, context)
