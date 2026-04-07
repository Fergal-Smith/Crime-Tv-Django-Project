from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShowList.as_view(), name='show_list'),
    path('<pk>/', views.ShowDetail.as_view(), name='show_detail'),
    path('create/', views.ShowCreate.as_view(), name='show_create'),
    path('update/<pk>/', views.ShowUpdate.as_view(), name='show_update'),
    path('delete/<pk>/', views.ShowDelete.as_view(), name='show_delete'),
]
