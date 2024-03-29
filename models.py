from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=70)
    author = models.CharField(max_length=150, default='*')
    number_of_pages = models.IntegerField()
    publish_date = models.DateField()
    quantity = models.IntegerField()
    
    def __str__(self):
        return self.author
