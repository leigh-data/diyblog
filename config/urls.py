from django.contrib import admin
from django.conf import settings
from django.urls import re_path, path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('blog.urls')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        re_path(r'^__debug__/', include(debug_toolbar.urls)), ] + urlpatterns
