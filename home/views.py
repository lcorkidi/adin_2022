from multiprocessing import context
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import LogInForm

class LogInView(View):

    template = 'home/login.html'
    form = LogInForm()

    def get(self, request):
        context = {'form': self.form}
        return render(request, self.template, context)

    def post(self, request):
        form = LogInForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user == None:
                msg = 'Usuario o clave errado(s).'
                context = {'form': self.form, 'msg': msg}
                return render(request, self.template, context)
            else:
                login(request, user)
                return redirect('home:user_home')
        else:
            context = {'form': self.form}
            return render(request, self.template, context)

class HomeView(LoginRequiredMixin, View):

    template = 'home/user_home.html'

    def get(self, request):
        return render(request, self.template)
