from django.db import models

# Create your models here.

class Club(models.Model):
    name = models.CharField(max_length=30)
    introduction = models.TextField(max_length=100)
    number=models.FloatField()

def __str__(self):
    return self.name


class Comment(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
    
    
    