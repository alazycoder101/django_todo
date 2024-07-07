from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=500)

    class Meta:
        db_table = 'notes'
    def __str__(self):
        return self.title
