from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # default home page for shows app
]
