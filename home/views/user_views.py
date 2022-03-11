from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.generic import View

from home.forms.User_forms import UserLogInForm

class UserLogInView(View):

    template = 'home/user_login.html'
    form = UserLogInForm()

    def get(self, request):
        context = {'form': self.form}
        return render(request, self.template, context)

    def post(self, request):
        form = UserLogInForm(request.POST or None)
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
