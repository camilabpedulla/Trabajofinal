from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponse


# Create your views here.

def login_web (request):

    if request.method == "POST":
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data.get("username")
            contraseña = formulario.cleaned_data.get("password")
            user = authenticate(username = usuario, password = contraseña)
            # Si el usuario y la contraseña son correctos
            if user is not None:
                login(request, user)
                return render (request, 'WebPage/index.html', {"mensaje" : f"Bienvenido {usuario}"})

            else :
                return HttpResponse ({"datos incorrectos"})

    # Si el usuario o la contraseña son incorrectos:

        else:
            return render (request, "log_web/login.html", {"formulario" : formulario})
    
    formulario = AuthenticationForm()
    
    return render (request, "log_web/login.html", {"formulario" : formulario})
 

    







    


