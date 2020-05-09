from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, Http404

def home(request):
    return HttpResponse("hello")

def index(request):
    return render(request,'main/index.html',context={})

# def signup(request):
#     return render(request,'superadmin/signup.html',context={})

