from django.shortcuts import render
from .models import Deportista, DeportistaForm, Participacion
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
import json
from django.core import serializers
from django.contrib.auth import authenticate, login, logout




# Create your views here.
def deportistas(request):
    deportistas_list = Deportista.objects.all()
    participaciones_list = Participacion.objects.all()
    context = {'deportistas_list': deportistas_list, 'participaciones_list': participaciones_list}
    return render(request, 'index.html', context)


def add_deportista(request):
    if request.method == 'POST':
        form = DeportistaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('deportista:deportistas'))
    else:
            form = DeportistaForm()
    return render(request, 'deportistas.html', {'form': form})

@csrf_exempt
def add_user_view(request):
    if request.method == 'POST':
        jsonUser = json.loads(request.body)
        user_Name = jsonUser['username']
        first_name = jsonUser['first_name']
        last_name = jsonUser['last_name']
        passwords = jsonUser['password']
        email = jsonUser['email']

        user_model = User.objects.create_user(username=user_Name, password=passwords)
        user_model.first_name = first_name
        user_model.last_name = last_name
        user_model.email = email
        user_model.save()
    return HttpResponse(serializers.serialize("json", [user_model]))

@csrf_exempt
def add_user(request):
    return(render(request,"register.html"))


@csrf_exempt
def login_view(request):
    print("Entro")
    if request.method == 'POST':
        jsonUser = json.loads(request.body)
        user_name = jsonUser['username']
        passwords = jsonUser['password']
        user = authenticate(username=user_name, password=passwords)
        if user is not None:
            login(request, user)
            message = "Ok"
        else:
            message = "Nombre de usuario o contraseña incorrecto"
    return JsonResponse({"message": message})

@csrf_exempt
def login_user(request):
    return render(request, "login.html")

@csrf_exempt
def logout_view(request):
    logout(request)
    return JsonResponse({"message": 'Ok'})