from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts_db={
    "suicide":"I belive I have always wanted to kill myself.",
    "loneliness":"Have ypu ever thought about being alone even in middle of full of people? I have and I feel terrible about it.",
    "hate": "I really hate myself and everything that happened in my life. ",

}
def start_page(request):
    return render(request,template_name='blog/start_page.html')


def posts(request):
    post_list=list(posts_db.keys())
    return render(request,template_name='blog/posts.html', context={'post_list':post_list})


def post(request,post_name):
    post_text=posts_db[post_name]
    return render(request,"blog/post.html",
                      {  "text":post_text,
                                "post_name":post_name})

