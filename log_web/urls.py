from django.urls import path
from log_web.views import login_web


urlpatterns = [
    path('login/', login_web, name="login"),
    
]