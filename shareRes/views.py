from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from .models import Category


# Create your views here.


def index(request):
    # return HttpResponse('Index')
    categories = Category.objects.all()
    content = {'categories': categories}
    return render(request, 'shareRes/index.html', content)


def restaurantDetail(request):
    # return HttpResponse('RestaurantDetail')
    return render(request, 'shareRes/restaurantDetail.html')


def restaurantCreate(request):
    # return HttpResponse('restaurantCreate')
    return render(request, 'shareRes/restaurantCreate.html')


def categoryCreate(request):
    # return HttpResponse('categoryCreate')
    categories = Category.objects.all()
    content = {'categories': categories}
    return render(request, 'shareRes/categoryCreate.html', content)


def Create_category(request):
    category_name = request.POST['categoryName']
    new_category = Category(category_name= category_name)
    new_category.save()
    return redirect('/')
    # return HttpResponse('category Create 기능을 구현하는 페이지')


def Delete_category(request):
    category_id = request.POST['categoryId']
    delete_category = Category.objects.get(id=category_id)
    delete_category.delete()
    return redirect('/')