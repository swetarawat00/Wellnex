from django.urls import path
from .views import RegisterView
from .views import RegisterView , ProtectedView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('test/', ProtectedView.as_view(), name='test'),
]
