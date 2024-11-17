from django.urls import path
from django.contrib.auth import views as auth_views

from .forms import LoginForm
from . import views



urlpatterns = [path("", views.UserProfile.as_view(), name="users-home"),
               path('register', views.RegisterView.as_view(), name='register'),
               path('login/',views.CustomLoginView.as_view(redirect_authenticated_user=True,
                                                        authentication_form=LoginForm), name='login'),
               path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
               path('password-reset/', views.ResetPasswordView.as_view(), name='password-reset'),
               path('password-reset-confirm/<uidb64>/<token>/',
                         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
                         name='password_reset_confirm'),
               path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
               path('profile/', views.ProfileDetailView.as_view(), name='users-profile'),
]
