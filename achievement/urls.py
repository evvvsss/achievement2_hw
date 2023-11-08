from django.urls import path
from . import views

urlpatterns = [
    path('numbers/', views.NumbersApi.as_view(), name='numbers'),
]