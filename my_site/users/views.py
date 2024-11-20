from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView
from django.views.generic.edit import View
from django.contrib.auth.views import LoginView, PasswordResetView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from .forms import RegisterForm,LoginForm, UpdateUserForm,UpdateProfileForm
from .models import Profile
# Create your views here.
class UserProfile(View):
    def get(self,request, *args, **kwargs):
        return render(request, template_name="users/home.html",context={"deneme":"Bu Benim Sayfam"})


class RegisterView(View):
    form_class=RegisterForm
    # initial = {'key': 'value'}
    template_name="users/register.html"

    def get(self,request):
        # form=self.form_class(initial=self.initial)
        form=self.form_class()
        return render(request,self.template_name,{"form":form})

    def post(self,request):
        form=self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            return redirect(to='/')

        return render(request, self.template_name, {'form': form})

    def dispatch(self, request, *args, **kwargs):
        # will redirect to the home page if a user tries to access the register page while logged in
        if request.user.is_authenticated:
            return redirect(to='users-home')

        # else process dispatch as it otherwise normally would
        return super(RegisterView, self).dispatch(request, *args, **kwargs)

class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'users/login.html'

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            # set session expiry to 0 seconds. So it will automatically close
            # the session after the browser is closed.
            self.request.session.set_expiry(0)

            # Set session as modified to force data updates/cookie to be saved.
            self.request.session.modified = True

            # else browser session will be as long as the session cookie time "SESSION_COOKIE_AGE"
            # defined in settings.py
        return super(CustomLoginView, self).form_valid(form)

class ResetPasswordView(SuccessMessageMixin,PasswordResetView):
    template_name = 'users/password_reset.html'
    email_template_name = 'users/password_reset_email.html'
    subject_template_name = 'users/password_reset_subject.txt'
    success_message = 'Your password has been reset.'
    success_url= reverse_lazy("login")


class ProfileDetailView(LoginRequiredMixin,DetailView):
    model = Profile
    template_name = 'users/profile.html'

    context_object_name = 'profile'

    def get_object(self, queryset=None):
        # Return the Profile of the currently logged-in user
        return self.request.user.profile


class ProfileUpdateView(LoginRequiredMixin,UpdateView):
    template_name = 'users/profile_update.html'
    success_url = reverse_lazy('users-profile')

    def get(self, request, *args, **kwargs):
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)
        return render(request, self.template_name, {'user_form': user_form, 'profile_form': profile_form})

    def post(self, request, *args, **kwargs):
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Your profile has been updated!')
            print('it is saved')
            return redirect('users-profile')
            print('it is saved2')
        return render(request, self.template_name, {'user_form': user_form, 'profile_form': profile_form})