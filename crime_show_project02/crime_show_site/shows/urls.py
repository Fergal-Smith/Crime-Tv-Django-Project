from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShowList.as_view(), name='show_list'),
    path('<int:pk>/', views.ShowDetail.as_view(), name='show_detail'),
    path('create/', views.ShowCreate.as_view(), name='show_create'),
    path('<int:pk>/update/', views.ShowUpdate.as_view(), name='show_update'),
    path('<int:pk>/delete/', views.ShowDelete.as_view(), name='show_delete'),
]
