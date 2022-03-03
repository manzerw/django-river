from django.contrib import admin
from django.urls.conf import re_path

urlpatterns = [
    re_path(r"^admin/", admin.site.urls),
]
