from django import forms
from . import models


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(
        widget=forms.PasswordInput
    )  # passwordinput 뿐.. 용도가 다르다 근데

    def clean(self):  # 종속되어 있으므로 생략 가능
        email = self.cleaned_data.get("email")  # 사용자가 입력한 값 중 email을 골라 저장함.
        password = self.cleaned_data.get("password")
        try:  # 실행 문구
            user = models.User.objects.get(email=email)  # 해당 이메일을 가진 유저를 user 저장
            if user.check_password(password):
                # user 모델의 정의된 check_password 메소드 사용
                # 주어진 string이 맞으면 True, 아니면 False
                return self.cleaned_data  # 다 맞다면, 입력한 email, password 데이터값 전달
            else:
                # 어디에 오류를 출력 할 지 정하기
                self.add_error("password", forms.ValidationError("Password is wrong"))
        except models.User.DoesNotExist:  # 실행 실패 시
            # 어디에 오류를 출력 할 지 정하기
            self.add_error("email", forms.ValidationError("User does not exist"))


class SignUpForm(forms.Form):
    pass
