from users import views as user_views
from django.urls import path

urlpatterns = [
    path('base/', user_views.BaseTemplateView.as_view()),
    path('register/', user_views.SignUpView.as_view()),
    path('index/', user_views.IndexTemplateView.as_view()),
]
