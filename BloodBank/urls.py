from django.urls import path

from . import views

urlpatterns = [
    path('', views.login),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('display/', views.display, name='display'),
    path('add_donor/', views.add_donor, name='add_donor'),
    path('logout/', views.logout, name='logout'),
    ]
