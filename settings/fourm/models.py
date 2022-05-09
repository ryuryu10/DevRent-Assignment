from django.db import models

class fourms(models.Model):
    title = models.CharField(max_length= 50)
    content = models.TextField()
    created_date = models.DateField(auto_now=True)
    