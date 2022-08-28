from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from log_web.forms import Customizacion_usuario
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def iniciar_sesion (request):

    if request.method == "GET":
        formulario = AuthenticationForm()
        context =  {
            "formulario":formulario
            }
        return render (request, "log_web/login.html", context)

    else:
        formulario = AuthenticationForm(request, data=request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            usuario = authenticate(username=data.get("username"), password=data.get("password"))

            if usuario is not None:
                login(request, usuario)
                return redirect ("inicio")

            else:
                context =  {
            "error": "Credenciales no validas",
            "formulario": formulario
            }
            return render (request, "log_web/login.html", context)

        else: 
            context =  {
            "error": "Formulario no valido",
            "formulario": formulario
            }
            return render (request, "log_web/login.html", context)


      
def registrar_usuario (request):
    if request.method == "GET":
        formulario = Customizacion_usuario()
        return render (request, "log_web/registro.html",{"formulario":formulario})

    else:
        formulario = Customizacion_usuario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect ("/WebPage/inicio")
        else:
          return render (request, "log_web/registro.html",{"formulario":formulario, "error": "Formulario no valido"})
        








    


