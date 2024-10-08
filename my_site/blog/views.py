from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def start_page(request):
    return render(request,template_name='blog/start_page.html')
