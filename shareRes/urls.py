
from django.contrib import admin
from django.urls import path, include
from .views import index, restaurantDetail, restaurantCreate, categoryCreate, Create_category, Delete_category
from .views import Create_restaurant

urlpatterns = [

  path('', index, name='index'),
  path('restaurantDetail/<str:res_id>', restaurantDetail, name='resDetailPage'),
  path('restaurantCreate/', restaurantCreate),
  path('restaurantCreate/create', Create_restaurant, name='resCreate'),
  path('categoryCreate/', categoryCreate),
  path('categoryCreate/create', Create_category, name='cateCreate'),
  path('categoryCreate/delete', Delete_category, name='cateDelete'),
]
