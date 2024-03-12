from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.say_hello) #views.say_hello is a reference and not a call to a function
]