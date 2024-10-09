from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts={
    "suicide":"I belive I have always wanted to kill myself.",
    "loneliness":"Have ypu ever thought about being alone even in middle of full of people? I have and I feel terrible about it.",
    "hate": "I really hate myself and everything that happened in my life. ",

}
def start_page(request):
    return render(request,template_name='blog/start_page.html')

def post(request):
    all_posts=list(posts.keys())
    return render(request,template_name='blog/all_posts.html', context={'all_posts':all_posts})

