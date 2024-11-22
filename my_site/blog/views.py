from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import date
from django.urls import reverse_lazy

from django.urls import reverse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView,DetailView,TemplateView,View

from .models import Post, StoredPost
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
    def is_stored_post(self, request, post_id):
        if request.user.is_authenticated:
            return StoredPost.objects.filter(user=request.user, post_id=post_id).exists()
        return False

    model = Post
    template_name = 'blog/post_detail.html'

    def get(self, request, post_id):
        post = Post.objects.get(id=post_id)

        context = {
            'post': post,
            'comment_form': CommentForm(initial={'user_name': request.user}),
            "post_tags": post.tag.all(),
            'comments': post.comments.all().order_by('-id'),
            'is_saved_for_later': self.is_stored_post(request, post.id),
        }
        return render(request, 'blog/post_detail.html', context=context)

    def post(self, request, post_id):
        action = request.POST.get('action')
        post = Post.objects.get(id=post_id)

        if action == 'save':
            if request.user.is_authenticated:
                StoredPost.objects.get_or_create(user=request.user, post=post)
        elif action == 'remove':
            if request.user.is_authenticated:
                StoredPost.objects.filter(user=request.user, post=post).delete()
        else:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.user_name = request.user
                comment.save()

        return HttpResponseRedirect(reverse('post_detail', args=[post_id]))



        context = {
            'post': post,
            'comment_form': CommentForm(initial={'user_name': request.user}),
            "post_tags": post.tag.all(),
            'comments': post.comments.all().order_by('-id'),
            'is_saved_for_later': self.is_stored_post(request, post.id),
        }
        return render(request, 'blog/post_detail.html', context=context)



class BlogPostView(LoginRequiredMixin, View):
    template_name = 'blog/blog_post.html'
    success_url = reverse_lazy("thank-you")

    def get(self, request):
        form = BlogPostForm(initial={'author': request.user})  # Author'ı initial olarak ata
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # Author'ı kaydet
            post.save()
            return redirect(self.success_url)  # Başarıyla kaydedildiyse yönlendir
        return render(request, self.template_name, {'form': form})




class ThankYouView(TemplateView):
    template_name="blog/thank_you.html"



class ReadLaterView(View):

        def get(self, request, *args, **kwargs):

            stored_posts = StoredPost.objects.filter(user=request.user)

            context = {

            }
            if stored_posts is None or len(stored_posts) == 0:
                context["stored_posts"] = []
                context['has_posts'] = False
            else:
                post_ids = stored_posts.values_list('post_id', flat=True)
                posts = Post.objects.filter(id__in=post_ids)
                context["posts"] = posts
                context['has_posts'] = True

            return render(request, 'blog/read_later_page.html',
                          context=context)

"""
def post(self, request):
            stored_posts = StoredPost.objects.filter(user=request.user)

            if stored_posts is None:
                stored_posts = []

            post_id = int(request.POST['post_id'])

            if post_id not in stored_posts:
                stored_posts.append(post_id)

            else:
                stored_posts.remove(post_id)
            request.session['stored_posts'] = stored_posts

            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
"""


