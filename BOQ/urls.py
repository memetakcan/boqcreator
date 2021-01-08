from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from Home.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_view, name="homesite"),
    path('', include('getboq.urls')),
    path('', include('setboq.urls')),
    path("accounts/",include(("accounts.urls")))
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)