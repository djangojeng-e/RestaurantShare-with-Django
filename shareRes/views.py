from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Category, Restaurant
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string


# Create your views here.


# def sendEmail(request):
#     checked_res_list = request.POST.getlist('checks')
#     inputReceiver = request.POST['inputReceiver']
#     inputTitle = request.POST['inputTitle']
#     inputContent = request.POST['inputContent']
#     restaurants = []
#     for checked_res_id in checked_res_list:
#         restaurants.append(Restaurant.objects.get(id=checked_res_id))
    
#     content = {'inputContent': inputContent, 'restaurants': restaurants}

#     msg_html = render_to_string('sendEmail/email_format.html', content)

#     msg = EmailMessage(subject = inputTitle, body=msg_html, from_email='headfat1218@gmail.com',
#                         bcc=inputReceiver.split(',')
#                       )
#     msg.content_subtype = 'html'
#     msg.send()
#     return HttpResponseRedirect(reverse('index'))

def index(request):
    # return HttpResponse('Index')
    categories = Category.objects.all()
    restaurants = Restaurant.objects.all()
    content = {'categories': categories,
               'restaurants': restaurants}
    return render(request, 'shareRes/index.html', content)


def restaurantDetail(request, res_id):
    # return HttpResponse('RestaurantDetail')
    restaurant = Restaurant.objects.get(id=res_id)
    content = {'restaurant': restaurant}
    return render(request, 'shareRes/restaurantDetail.html', content)


def restaurantCreate(request):
    # return HttpResponse('restaurantCreate')
    categories = Category.objects.all()
    content = {'categories': categories}
    return render(request, 'shareRes/restaurantCreate.html', content)


def Delete_restaurant(request):
    res_id = request.POST['resId']
    restaurant = Restaurant.objects.get(id=res_id)
    restaurant.delete()
    return HttpResponseRedirect(reverse('index'))


def Create_restaurant(request):
    category_id = request.POST['resCategory']
    category = Category.objects.get(id=category_id)
    name = request.POST['resTitle']
    link = request.POST['resLink']
    content = request.POST['resContent']
    keyword = request.POST['resLoc']
    new_res = Restaurant(category=category, restaurant_name=name,
                        restaurant_link=link, restaurant_content=content, restaurant_keyword=keyword)
    new_res.save()
    return redirect('/')


def categoryCreate(request):
    # return HttpResponse('categoryCreate')
    categories = Category.objects.all()
    content = {'categories': categories}
    return render(request, 'shareRes/categoryCreate.html', content)


def restaurantUpdate(request, res_id):
    # return HttpResponse("restaurant를 수정할 페이지")
    categories = Category.objects.all()
    restaurant = Restaurant.objects.get(id=res_id)
    content = {'categories': categories, 'restaurant': restaurant}
    return render(request, 'shareRes/restaurantUpdate.html', content)


def Update_restaurant(request):
    resId = request.POST['resId']
    change_category_id = request.POST['resCategory']
    change_category = Category.objects.get(id=change_category_id)
    change_name = request.POST['resTitle']
    change_link = request.POST['resLink']
    change_content = request.POST['resContent']
    change_keyword = request.POST['resLoc']
    before_restaurant = Restaurant.objects.get(id=resId)
    before_restaurant.category = change_category
    before_restaurant.restaurant_name = change_name
    before_restaurant.restaurant_link = change_link
    before_restaurant.restaurant_content = change_content
    before_restaurant.restaurant_keyword = change_keyword
    before_restaurant.save()
    return HttpResponseRedirect(reverse('resDetailPage', kwargs={'res_id': resId}))


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

