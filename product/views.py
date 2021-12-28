from django.http import response
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.base import View

class Home(TemplateView):
    template_name = 'index.html'

class Product(View):
    def get(self,request):
        return render(request,'product.html')

class Blog(TemplateView):
    template_name = 'blog.html'

# class Home(TemplateView):
#     template_name = 'blog.html'