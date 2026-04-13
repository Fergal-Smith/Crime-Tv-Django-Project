from django.urls import path
from .views import ReviewList, ReviewCreate
from .views import submit_rating

urlpatterns = [
    path('', ReviewList.as_view(), name='review_list'),
    path('create/', ReviewCreate.as_view(), name='review_create'),
    path('rate/<int:show_id>/', submit_rating, name='submit_rating'),
]
