from django import forms
from . import models as user_models
from .utils.manage import UserManager
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField

user_models.MyUser = get_user_model()


class RegisterForm(forms.ModelForm):
    """
    The default
    """
    password = forms.CharField(widget=forms.PasswordInput)
    password_2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    class Meta:
        model = user_models.MyUser
        fields = ['email']

        def clean_email(self):
            """
            Verify email is available.
            """
            email = self.cleaned_data.get('email')
            qs = user_models.MyUser.objects.filter(email=email)
            if qs.exists():
                raise forms.ValidationError("email is taken")
            return email


