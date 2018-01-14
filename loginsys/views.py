from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response
from django.template.context_processors import csrf
from django.views.generic import View
from django.contrib.auth.models import User
from datetime import datetime
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.forms import EmailField, CharField



def function_view(request):
    return HttpResponse('response from func view')


class ClassBased(View):
    def get(self, request):
        return HttpResponse('response from class based view')


class CustomUserCreationForm(UserCreationForm):
    email = EmailField(label=("Email adress"), required=True, help_text=("Required."))
    firstname = CharField(label=("firstname"), max_length=20, min_length=1, required=True)
    lastname = CharField(label=("lastname"), max_length=20, min_length=1, required=True)

    class Meta:
        model = User
        fields = ("username", "email",
                  # "password1", "password2",
                  "firstname", "lastname")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.firstname = self.cleaned_data["firstname"]
        user.lastname = self.cleaned_data["lastname"]
        if commit:
            user = User.objects.create_user(username=user.username,
                                            password=user.password,
                                            email=user.email,
                                            last_name=user.lastname,
                                            first_name=user.firstname)
            #user.save()
        return user

def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('main')
        else:
            args['login_error'] = "Пользователь не найден"
            return render_to_response('login.html',args)

    else:
        return render_to_response('login.html',args)


def logout(request):
    auth.logout(request)
    return redirect('main')


def register(request):
    args = {}
    #args.update(csrf(request))
    args['form'] = CustomUserCreationForm()
    if request.POST:
        newuser_form = CustomUserCreationForm(request.POST)
        if newuser_form.is_valid():
            #newuser_form.save()
            #newuser = auth.authenticate(username=newuser_form.cleaned_data['username'], password=newuser_form.cleaned_data['password2'])
            # import pdb
            # pdb.set_trace()
            #auth.login(request, newuser)
            user = newuser_form.save()
            auth.login(request, user)
            return redirect('main')
        else:
            args['error_messages'] = newuser_form.error_messages
            args['form'] = newuser_form
    return render(request, 'register.html', args)


def register2(request):
    errors = {}
    #errors.update(csrf(request))
    if request.method == 'POST':
        username = request.POST.get('username')
        if not username:
            errors['username'] = 'Введите логин'
        elif len(username) < 5:
            errors['username'] = 'Логин минимум 5 символов'
        elif User.objects.filter(username=username).exists():
            errors['username'] = 'Такой логин уже существует'
        password = request.POST.get('password')
        if not password:
            errors['password'] = 'Введите пароль'
        elif len(password) < 8:
            errors['password'] = 'Пароль не меньше 8 символов'
        password_repeat = request.POST.get('password2')
        if password != password_repeat:
            errors['password2'] = 'Пароли должны совпадать'
        email = request.POST.get('email')
        if not email:
            errors['email'] = 'Введите e-mail'
        firstname = request.POST.get('firstname')
        if not firstname:
            errors['firstname'] = 'Введите имя'
        surname = request.POST.get('surname')
        if not surname:
            errors['surname'] = 'Введите фамилию'
        if not errors.keys():
            user = User.objects.create_user(username=username,
                                            password=password,
                                            email=email,
                                            first_name=firstname,
                                            last_name=surname)
            return HttpResponseRedirect('/')
    return render(request, 'register2.html', errors)


