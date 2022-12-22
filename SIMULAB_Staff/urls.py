from django.contrib import admin
from django.conf.urls import include
from django.urls import path

urlpatterns = [
    path('blog/', include('blog.urls')),
    path('', include('single_pages.urls')),
    path('admin/', admin.site.urls),
]