from django.db import models

# Create your models here.
class Tasks(models.Model):
    title = models.CharField(max_length=200,default="title")
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"
    
    
