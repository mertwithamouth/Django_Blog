from django.shortcuts import render, redirect
from django.views.generic.edit import View
from django.contrib import messages
from .forms import RegisterForm
# Create your views here.
class UserProfile(View):
    def get(self,request, *args, **kwargs):
        return render(request, template_name="users/profile.html",context={"deneme":"Bu Benim Sayfam"})


class RegisterView(View):
    form_class=RegisterForm
    initial = {'key': 'value'}
    template_name="users/register.html"

    def get(self,request):
        form=self.form_class(initial=self.initial)
        return render(request,self.template_name,{"form":form})

    def post(self,request):
        form=self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            return redirect(to='/')

        return render(request, self.template_name, {'form': form})