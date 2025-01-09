from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Alpha Apartments API",
        description="An Apartment Management API for Real Estate",
        default_version="v1",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("api/v1/auth/", include("djoser.urls")),
    path("api/v1/auth/", include("core_apps.users.urls")),
    path("api/v1/profiles/", include("core_apps.profiles.urls")),
    path("api/v1/apartments/", include("core_apps.apartments.urls")),
    path("api/v1/issues/", include("core_apps.issues.urls")),
    path("api/v1/reports/", include("core_apps.reports.urls")),
    path("api/v1/ratings/", include("core_apps.ratings.urls")),
    path("api/v1/posts/", include("core_apps.posts.urls")),
    path(settings.ADMIN_URL, admin.site.urls),
    path("redoc/",schema_view.with_ui("redoc", cache_timeout=0),name="schema-redoc",),
]

admin.site.site_header = "Alpha Apartments Admin"
admin.site.site_title = "Alpha Apartments Admin Portal"
admin.site.index_title = "Welcome to Alpha Apartments Admin Portal"
