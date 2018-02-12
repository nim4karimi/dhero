from django.urls import path

# import from polls view
from . import views

urlpatterns = [
    path("", views.index , name="index"),
]