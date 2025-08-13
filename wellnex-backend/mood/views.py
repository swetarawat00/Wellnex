from rest_framework import viewsets, permissions
from .models import Mood
from .serializers import MoodSerializer

class MoodViewSet(viewsets.ModelViewSet):
    serializer_class = MoodSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Mood.objects.filter(user=self.request.user).order_by('-created_at')
    
    def perform_create(self , serializer):
        serializer.save(user=self.request.user)
