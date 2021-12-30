from django.shortcuts import render
from django.views.generic.base import View

class Register(View):
    def get(self,request):
        return render(request,"register.html")

class Login(View):
    def get(self,request):
        return render(request,"login.html")

class Profile(View):
    def get(self,request):
        return render(request,'profile.html')