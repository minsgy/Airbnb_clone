from django import forms
from . import models


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(
        widget=forms.PasswordInput
    )  # passwordinput 뿐.. 용도가 다르다 근데

    def clean_email(self):
        # 무엇을 검색할 때,method 이름은 무조건 clean_(필드이름) << 이여야함.
        # 에러 출력용 및 데이터 정리
        # return 안하면 값삭제됨.
        email = self.cleaned_data.get("email")  # 사용자가 입력한 값 중 email을 골라 저장함.
        try:  # 실행 문구
            models.User.objects.get(username=email)
            return email
        except models.User.DoesNotExist:  # 실행 실패 시
            raise forms.ValidationError("User does not exist")

    def clean_password(self):
        print("clean password")
