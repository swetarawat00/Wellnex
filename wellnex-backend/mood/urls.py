from rest_framework.routers import DefaultRouter
from .views import MoodViewSet
from django.urls import path, include

router = DefaultRouter()
router.register('moods' , MoodViewSet , basename= 'moods')

urlpatterns = [
    path('',include(router.urls))
]