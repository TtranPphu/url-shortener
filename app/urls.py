from django.urls import path
from . import views

urlpatterns = [
    path("<str:short_code>", views.auto_redirect, name="auto_redirect"),
    path("shorten", views.shorten_create, name="shorten_create"),
    path("shorten/<str:short_code>", views.shorten, name="shorten_edit"),
]
