from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(
        widget=forms.PasswordInput
    )  # passwordinput 뿐.. 용도가 다르다 근데

