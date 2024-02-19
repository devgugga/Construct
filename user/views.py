from django.http import HttpResponse
from django.shortcuts import render
from rolepermissions.decorators import has_permission_decorator
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import auth

from .models import Users


@has_permission_decorator("register_seller")
def register_seller(request):
    if request.method == "GET":
        return render(request, "register_seller.html")
    if request.method == "POST":
        name = request.POST.get("username")
        surname = request.POST.get("surname")
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = Users.objects.filter(email=email)

        if user.exists():
            # TODO: Utilizar messages do django
            return HttpResponse("Já existe um usuário com esse e-mail")

        user = Users.objects.create_user(
            username=name,
            email=email,
            password=password,
            first_name=name,
            last_name=surname,
            role="V",
        )

        # TODO: Redirecionar com uma mensagem
        return HttpResponse("Conta Criada")


def login(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect(reverse("register_seller"))
        return render(request, "login.html")
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = auth.authenticate(username=username, password=password)

        if not user:
            # TODO: Redirecionar com mensagem de erro
            return HttpResponse("Usuário não encontrado no banco de dados")

        auth.login(request, user)
        return HttpResponse("Logado com sucesso")


def logout(request):
    request.session.flush()
    return redirect(reverse("login"))
