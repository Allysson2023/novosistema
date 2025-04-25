from contact import views
from django.urls import path


urlpatterns = [
    path('', views.index),
]