from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add_address", views.add_address, name="add_address"),
    path("clear_all", views.clear_all, name="clear_all")
    
]
