from django.urls import path
from . import views
from .views import ShowList, ShowDetail
from .views import HomeView
from .views import ShowCreate

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('shows/', ShowList.as_view(), name='show_list'),
    path('<int:pk>/', views.ShowDetail.as_view(), name='show_detail'),
    path('show/add/', ShowCreate.as_view(), name='show_add'),
    path('<int:pk>/update/', views.ShowUpdate.as_view(), name='show_update'),
    path('<int:pk>/delete/', views.ShowDelete.as_view(), name='show_delete'),
]
