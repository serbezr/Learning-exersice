
from django.urls import path
from .views import *

urlpatterns = [
    path('', index),  # http://127.0.0.1:8000/
    path('cats/<int:catid>/',categories), #http://127.0.0.1:8000/cats/1/
]