from rest_framework import serializers
from .models import Mood

class MoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mood
        fields = '__all__'
        read_only_fields = ['user' , 'created_at']
        