from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("<str:shortened_url>", views.auto_redirect, name="redirect"),
    path("shorten", views.set_shorten, name="shorten"),
    path("shorten/<str:shortened_url>", views.shorten, name="shorten"),
]
