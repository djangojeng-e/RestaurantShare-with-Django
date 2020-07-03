from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.


def sendEmail(request):
    checked_res_list = request.POST.getlist('checks')
    inputReceiver = request.POST['inputReceiver']
    inputTitle = request.POST['inputTitle']
    inputContent = request.POST['inputContent']
    print(checked_res_list, "/", inputReceiver, "/", inputTitle, "/", inputContent)
    return HttpResponseRedirect(reverse('index'))
    # return HttpResponse('sendEmail')
