from django import forms
from crispy_forms.helper import FormHelper
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    helper = FormHelper()
    helper.form_show_labels = False
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Parol",
                               widget=forms.PasswordInput)
    password_2 = forms.CharField(label="Parol takrorlang",
                               widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']

    def clean_password2(self):
        data = self.cleaned_data
        if data["password"] != data["password2"]:
            raise forms.ValidationError("IKkala parolingiz ham bir-biriga teng bo'lishi kerak")

