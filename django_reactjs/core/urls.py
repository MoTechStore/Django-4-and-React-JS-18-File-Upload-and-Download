from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FilesViewSet

router = DefaultRouter()
router.register('files', FilesViewSet, basename='files')


urlpatterns = [
    path('api/', include(router.urls)),
]
