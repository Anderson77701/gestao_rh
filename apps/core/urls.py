from django.urls import path
from .views import homeCore

urlpatterns = [
    path('', homeCore),
]