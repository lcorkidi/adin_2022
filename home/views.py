import django
from django.shortcuts import render
from django.views.generic import View
from .forms import LogInForm

class LogInView(View):

    template = 'home/login.html'
    form = LogInForm()

    def get(self, request):
        context = {'form': self.form}
        return render(request, self.template, context)

