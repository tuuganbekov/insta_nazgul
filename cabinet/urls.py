from django.urls import path
from .views import get_cabinet


urlpatterns = [
    path('', get_cabinet)
]