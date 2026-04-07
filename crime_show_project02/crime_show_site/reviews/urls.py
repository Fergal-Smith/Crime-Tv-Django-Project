from django.urls import path
from .views import ReviewList, ReviewCreate

urlpatterns = [
    path('', ReviewList.as_view(), name='review_list'),
    path('add/', ReviewCreate.as_view(), name='review_create'),
]
