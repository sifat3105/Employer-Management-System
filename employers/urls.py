from django.urls import path
from . import views

urlpatterns = [
    path('employers/', views.EmployerListCreate.as_view()),
    path('employers/<int:pk>/', views.EmployerDetail.as_view()),
]
