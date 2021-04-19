"""DjangoAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from user import views

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework.routers import DefaultRouter

# from rest_framework.documentation import include_docs_urls

from user.apis import MusicViewSet, BookViewSet
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

router = DefaultRouter()
router.register("music", MusicViewSet, basename="api-music")
router.register("book", BookViewSet, basename="api-book")

schema_view = get_schema_view(
    openapi.Info(
        title="Rick API Test",
        default_version="v1",
        description="Test descriptionnnnnnnnnnnnnnnnnnnnnnnnn",
        terms_of_service="https://portal.wistron.com/",
        contact=openapi.Contact(email="Rick_Wu@wistron.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include((router.urls, "api"), namespace="api")),
    # path("api/docs/", get_swagger_view(title="Rick API TEST")),
    path(
        "api/swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(
        "api/docs/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
    ),
]
