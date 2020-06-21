
from django.contrib import admin
from django.urls import path, include
from .views import index, restaurantDetail, restaurantCreate, categoryCreate, Create_category, Delete_category


urlpatterns = [

  path('', index, name='index'),
  path('restaurantDetail/', restaurantDetail),
  path('restaurantCreate/', restaurantCreate),
  path('categoryCreate/', categoryCreate),
  path('categoryCreate/create', Create_category, name='cateCreate'),
  path('categoryCreate/delete', Delete_category, name='cateDelete'),
]
