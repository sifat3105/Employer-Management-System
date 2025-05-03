from django.urls import path
from . import views

urlpatterns = [
    path('auth/signup/', views.SignUpView.as_view()),
    path('auth/login/', views.LoginView.as_view()),
    path('auth/logout/', views.LogoutView.as_view()),
    path('auth/profile/', views.ProfileView.as_view()),
]
