from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from core.views import DashboardView, HomePageView
from core import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('dashbord/', DashboardView.as_view(), name='dashbord'),
    path("", include("storage.urls")),
    path("", include("hosting.urls")),
    path("", include("support.urls")),
    path("", include("users.urls")),
    path("", include("billing.urls")),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
urlpatterns += staticfiles_urlpatterns()