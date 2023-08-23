from django.urls import path
from .views import index

urlspatterns = [
    path('', index)
]