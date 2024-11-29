from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name="usuarios_view"),
    path('login/', views.login_view, name="login_view"),
    path('registro/', views.registro_view, name="registro_view"),
    path('logout/', views.logout_view, name="logout_view"),
]