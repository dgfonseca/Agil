from django.shortcuts import render
from .models import Deportista, DeportistaForm, Participacion
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
import json
from django.core import serializers
from django.contrib.auth import authenticate, login, logout
from django.views import generic





class DeportistaListView(generic.ListView):
    model = Deportista

def participaciones(request):
    participaciones_list = Participacion.objects.all()
    context = {'participacion_list':participaciones_list}
    return render(request,'olimpicos/deportista_detail.html',context)




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


class DeportistaDetailView(generic.DetailView):
    model = Deportista

    def get_context_data(self, **kwargs):
        context = super(DeportistaDetailView, self).get_context_data(**kwargs)
        context['participacion_list'] = Participacion.objects.all()
        return context

