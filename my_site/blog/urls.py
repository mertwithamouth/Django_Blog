from django.urls import path
from . import views



urlpatterns = [path("", views.StartPage.as_view(), name='start_page'),
                path("posts", views.AllPostsListView.as_view() , name='posts'),
                path("posts/<slug:slug>", views.PostDetailView.as_view() , name="post_detail"),
                path("create-post", views.BlogPostView.as_view(), name="create-post"),
                path("thank-you", views.ThankYouView.as_view()),
               ]