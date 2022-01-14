from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User

@csrf_exempt
def auth_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']


        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('dashboard:dashboard'))
        # elif not user.is_active:
        #     messages.add_message(request, 30, 'Sua conta não esta ativa.')
        else:
            messages.add_message(request, 20, 'Usuário ou senha inválidos')

    return render(request, 'login/login.html', {})

@csrf_exempt
def cadastro(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if username:
            if not username_exists(username):
                User.objects.create_user(username=username, password=password)
                messages.success(request, f"Usuário {username} criado com sucesso")

                return redirect('login:login')
            else:
                messages.add_message(request, 20, 'Este usuário já existe')
        else:
            messages.add_message(request, 30, 'Necessita especificar um nome de usuário')

    return render(request, 'login/cadastro.html', {})

def log_out(request):
    logout(request)
    messages.success(request, "Deslogado com sucesso")
    return HttpResponseRedirect(reverse('login:login'))


def username_exists(username):
    return User.objects.filter(username=username).exists()