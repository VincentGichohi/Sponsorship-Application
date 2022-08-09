from django.shortcuts import render
from users import models as user_models
from users import forms as user_forms
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy


class SignUpView(SuccessMessageMixin, CreateView):
    template_name = 'register.html'
    success_url = reverse_lazy('login')
    form_class = user_forms.RegisterForm
    success_message = 'Your account has been created successfully.'
