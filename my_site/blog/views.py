from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from datetime import date

from django.urls import reverse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView,DetailView,TemplateView,View

from .models import Post
from .forms import BlogPostForm,CommentForm
# Create your views here.


# def start_page(request):
#     sorted_posts=Post.objects.all().order_by('-date')[:3]
#
#     return render(request,template_name='blog/start_page.html', context={'posts_db':sorted_posts})

class StartPage(ListView):
    model = Post
    template_name = 'blog/start_page.html'

    def get_context_data(self, **kwargs):
        context=super().get_context_data()
        context['posts_db']=Post.objects.all().order_by('-date')[:3]
        return context



# def posts(request):
#     posts_db = Post.objects.all()
#     return render(request,template_name='blog/all_posts.html', context={'post_list':posts_db})


#Burada biraz daha farkli bir yontem uygulayacagim orderlamak icin
class AllPostsListView(ListView):
    model = Post
    template_name = 'blog/all_posts.html'
    context_object_name = 'post_list'
    ordering = ['title']




# def post_detail(request,slug):
#     try:
#         identifed_post=Post.objects.get(slug=slug)
#         return render(request,"blog/post_detail.html",
#                     {'post':identifed_post,
#                      'post_tags':identifed_post.tag.all()})
#     except:
#         # raise Http404()
#         return render(request, "404.html")


class PostDetailView(View):
    model = Post
    template_name = 'blog/post_detail.html'


    def get(self, request, slug):
        post=Post.objects.get(slug=slug)
        context = {
            'post':post,
            'comment_form':CommentForm(),
            "post_tags":post.tag.all()
        }
        return render(request, 'blog/post_detail.html',
                      context=context)

    def post(self, request,slug):
        form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=post
            comment.save()
            #return HttpResponseRedirect('/thank-you')
            return HttpResponseRedirect(reverse('post_detail', args=[slug]))

        context = {
            'post': post,
            'comment_form': CommentForm(),
            "post_tags": post.tag.all
        }
        return render(request, 'blog/post_detail.html',
                      context=context)




class BlogPostView(CreateView):
    model = Post
    form_class = BlogPostForm
    template_name = 'blog/blog_post.html'
    success_url = "thank-you"

class ThankYouView(TemplateView):
    template_name="blog/thank_you.html"
