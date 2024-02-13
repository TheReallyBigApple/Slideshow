from django.urls import path
from ss_app import views

urlpatterns = [
    path("", views.home, name='home'),
]