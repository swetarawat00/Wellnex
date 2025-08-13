from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Mood(models.Model):
    MOOD_CHOICES=[
        ('happy','Happy'),
        ('sad','Sad'),
        ('neutral','Neutral'),
        ('angry','Angry'),
        ('anxious','Anxious'),
        ('excited','Excited'),
    ]

    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name='moods')
    mood = models.CharField(max_length=20 , choices=MOOD_CHOICES)
    note = models.TextField(blank=True, null =True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}- {self.mood} ({self.created_at.date()})"


