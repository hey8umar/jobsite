from django.urls import path

from . import views

urlpatterns = [
    path("<str:job>", views.index)
]