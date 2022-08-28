from django.urls import path
from log_web.views import iniciar_sesion, registrar_usuario
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('inicar_sesion/', iniciar_sesion, name="Iniciar"),
    path('registrar_usuario/', registrar_usuario, name="Registrarse"),
    path('cerrar_sesion/', LogoutView.as_view(template_name= "log_web/logout.html"), name="cerrar_sesion")
]