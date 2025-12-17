from django.urls import path, include
from . import views


urlpatterns = [
    path("shop/", views.index, name="index")
]