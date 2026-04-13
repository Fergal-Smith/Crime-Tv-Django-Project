from django.contrib import admin
from django.urls import path, include
from reviews.views import SignUpView
from shows.views import ShowList
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    path('', ShowList.as_view(), name='home'),
    path('shows/', include('shows.urls')),
    path('reviews/', include('reviews.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)