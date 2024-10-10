from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts_db={
    "Suicide":["I belive I have always wanted to kill myself.","https://picsum.photos/id/1069/150/150"],
    "Loneliness":["Have ypu ever thought about being alone even in middle of full of people? I have and I feel terrible about it.",
                  "https://picsum.photos/id/1074/150/150"],
    "Hate": ["I really hate myself and everything that happened in my life. ", "https://picsum.photos/id/1011/150/150"],

}
def start_page(request):
    post_list = list(posts_db.keys())
    return render(request,template_name='blog/start_page.html', context={'posts_db':posts_db})


def posts(request):
    post_list=list(posts_db.keys())
    return render(request,template_name='blog/posts.html', context={'post_list':post_list})


def post(request,post_name):
    post_text=posts_db[post_name][0]
    return render(request,"blog/post.html",
                      {  "text":post_text,
                                "post_name":post_name})

