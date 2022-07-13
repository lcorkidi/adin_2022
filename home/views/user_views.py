from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from home.forms.User_forms import UserLogInForm
from adin.utils.user_data import user_group_str

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

class UserLogOutView(View):

    def get(self, request):
        logout(request)
        return redirect('home:user_login')

class UserCreationView(LoginRequiredMixin, PermissionRequiredMixin, View):

    template = 'home/user_create.html'
    form = UserCreationForm
    title = 'Usuario'
    subtitle = 'Crear'
    permission_required = 'auth.add_user'
    
    def get(self, request):
        form = self.form()
        context = {'form': form, 'title': self.title, 'subtitle': self.subtitle, 'group': user_group_str(request.user)}
        return render(request, self.template, context)

    def post(self, request):
        form = self.form(request.POST)
        if not form.is_valid():
            context = {'form': form, 'title': self.title, 'subtitle': self.subtitle, 'group': user_group_str(request.user)}
            return render(request, self.template, context)
        form.save()            
        return redirect('home:user_home')

class UserPasswordChangeView(LoginRequiredMixin, PermissionRequiredMixin, View):

    template = 'home/user_create.html'
    form = PasswordChangeForm
    title = 'Usuario'
    subtitle = 'Cambiar Clave'
    permission_required = 'auth.change_user'
    
    def get(self, request):
        form = self.form(request.user)
        context = {'form': form, 'title': self.title, 'subtitle': self.subtitle, 'group': user_group_str(request.user)}
        return render(request, self.template, context)

    def post(self, request):
        form = self.form(request.user, request.POST)
        if not form.is_valid():
            print(form.error_messages)
            context = {'form': form, 'title': self.title, 'subtitle': self.subtitle, 'group': user_group_str(request.user)}
            return render(request, self.template, context)
        form.save()
        update_session_auth_hash(request, form.user)            
        return redirect('home:user_home')
