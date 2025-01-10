from django.contrib.auth.models import User
from django.db import models

class ChatGptPrompts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ChatGptPrompts')
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)


    def __str__(self):
        return self.question
