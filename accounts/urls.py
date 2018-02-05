#accounts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name="signup"),
    path('profile/<int:id>', views.Profile.as_view(), name="profile"),
]