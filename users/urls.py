from users import views as user_views
from django.urls import path

urlpatterns = [
    path('', user_views.BaseTemplateView.as_view()),
    path('register/', user_views.SignUpView.as_view()),

]
