from django.shortcuts import render
from django.http import HttpResponse
from datetime import date

from .models import Post


# Create your views here.


def get_date(post):
    return post["date"]
def start_page(request):
    sorted_posts=Post.objects.all().order_by('date')

    return render(request,template_name='blog/start_page.html', context={'posts_db':sorted_posts})


def posts(request):
    posts_db = Post.objects.all()
    return render(request,template_name='blog/all_posts.html', context={'post_list':posts_db})





def post_detail(request,slug)
    try:
        identifed_post=Post.objects.get(slug=slug)
        return render(request,"blog/post_detail.html",
                    {'post':identifed_post})
    except:
        # raise Http404()
        return render(request, "404.html")

