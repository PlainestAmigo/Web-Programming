from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("shrayash", views.shrayash, name="shrayash"),
    path("<str:name>", views.greet, name="greet")
]