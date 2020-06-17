
from django.contrib import admin
from django.urls import path, include
from .views import sendEmail

urlpatterns = [
    path('send/', sendEmail),
]
