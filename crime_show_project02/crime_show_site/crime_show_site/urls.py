from django.contrib import admin
from django.urls import path, include
from reviews.views import SignUpView
from shows.views import ShowList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    path('', ShowList.as_view(), name='home'),
    path('shows/', include('shows.urls')),
    path('reviews/', include('reviews.urls')),
]
