from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView
from django.contrib.auth import login, logout, authenticate
from . import forms

# User 로그인법
# 1번 인증 authenticate(request, username 필요함!!, password 필요함!!)
# 2번 로그인 request, user


# Create your views here.
class LoginView(FormView):  # username을 필요로함!

    template_name = "users/login.html"
    form_class = forms.LoginForm
    success_url = reverse_lazy("core:home")  # 필요할 때 실행 하는것

    def form_valid(self, form):  # form 유효성 체크
        email = form.cleaned_data.get("email")  # 유효 시 입력 값을 저장
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)  # 인증 절차
        if user is not None:
            login(self.request, user)  # 로그인
        return super().form_valid(form)  # 실행하면 알아서 success_url로감

    # initial = {
    #     'email': "minseok@naver.com",
    # }
    # def get(self, request): # 처음 들어갈 때
    #     form = forms.LoginForm()
    #     return render(request, "users/login.html", {"form": form})

    # def post(self, request):
    #     form = forms.LoginForm(request.POST)
    #     if form.is_valid():  # 유효한 값 인지 검사
    #         email = form.cleaned_data.get("email")  # 유효 시 입력 값을 저장
    #         password = form.cleaned_data.get("password")
    #         user = authenticate(request, username=email, password=password) # 인증 절차
    #         if user is not None:
    #             login(request, user) # 로그인
    #             return redirect(reverse("core:home"))
    #     return render(request, "users/login.html", {"form": form})


def log_out(request):
    logout(request)
    return redirect(reverse("core:home"))


class SignUpView(FormView):
    template_name = "users/signup.html"
    form_class = forms.SignUpForm
    success_url = reverse_lazy("core:home")  # 필요할 때 실행 하는것
