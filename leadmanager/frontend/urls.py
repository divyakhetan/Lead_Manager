from django.urls import path
from . import views

urlpatterns = [
    # about the index method that we made in views.py
    path('',views.index)
]