from django.shortcuts import render, redirect, reverse
from django.views import View
from django.contrib.auth import login, logout, authenticate
from . import forms

# User 로그인법
# 1번 인증 authenticate(request, username 필요함!!, password 필요함!!)
# 2번 로그인 request, user


# Create your views here.
class LoginView(View):
    def get(self, request): # 처음 들어갈 때
        form = forms.LoginForm()
        return render(request, "users/login.html", {"form": form})

    def post(self, request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():  # 유효한 값 인지 검사
            email = form.cleaned_data.get("email")  # 유효 시 입력 값을 저장
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=email, password=password) # 인증 절차
            if user is not None:
                login(request, user) # 로그인
                return redirect(reverse("core:home"))
        return render(request, "users/login.html", {"form": form})


def log_out(request):
    logout(request)
    return redirect(reverse("core:home"))
