from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import HttpResponseRedirect
# Create your views here.



def index(request):
    return HttpResponseRedirect(reverse('App_Blog:blog_list'))
