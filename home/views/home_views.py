from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import View

from adin.utils.user_data import user_group_str

class HomeView(LoginRequiredMixin, View):

    template = 'home/user_home.html'
    title = 'Inicio'

    def get(self, request):
        context = {'title': self.title, 'group': user_group_str(request.user)}
        return render(request, self.template, context)
