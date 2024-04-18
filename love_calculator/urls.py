from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('calculate_love',views.calculate_love, name='calculate_love'),

]
