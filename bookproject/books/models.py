from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)  # 투표 수 추가

    def __str__(self):
        return f"{self.title} by {self.author}"