from django import forms
from .models import MyUser
from .utils.manage import UserManager
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField

MyUser = get_user_model()


class RegisterForm(forms.ModelForm):
    """
    The default
    """
    password = forms.CharField(widget=forms.PasswordInput)
    password_2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ['email']

        def clean_email(self):
            """
            Verify email is available.
            """
            email = self.cleaned_data.get('email')
            qs = MyUser.objects.filter(email=email)
