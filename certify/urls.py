from django.urls import path
from . import views

app_name = 'certify'

urlpatterns = [
    path('', views.index, name='index'),
    path('pagar/', views.pagar, name='pagar'),
]