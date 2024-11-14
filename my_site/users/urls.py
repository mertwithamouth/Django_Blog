from django.urls import path
from . import views



urlpatterns = [path("", views.UserProfile.as_view()),
               path('register', views.RegisterView.as_view(), name='users-register'),  # This is what we added
]
