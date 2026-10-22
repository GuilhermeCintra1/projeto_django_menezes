from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateField(auto_now_add=True)
    content = models.TextField()
  


    def __str__(self):
        return f'{self.id}. {self.title}'
    
    