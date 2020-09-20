from django.shortcuts import render
from django.views import View
from . import forms

# Create your views here.
class LoginView(View):
    def get(self, request):
        form = forms.LoginForm()
        return render(request, "users/login.html", {"form": form})

    def post(self, request):
        form = forms.LoginForm(request.POST)
<<<<<<< HEAD
        if form.is_valid():  # clean_(data)은 리턴하지않으면 값이 삭제됌.

            print(form.cleaned_data)
        return render(request, "users/login.html", {"form": form})
=======
        return render(request, "users/login.html",{"form": form})
>>>>>>> 323c4eca30edd8f678d9cf0242ea7e25e6e7a572
