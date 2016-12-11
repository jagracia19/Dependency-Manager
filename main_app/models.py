from django.db import models
from django.conf import settings

UPLOADS_DIR = getattr(settings, "UPLOADS_DIR", "uploads")

class File(models.Model):    
    
    name = models.CharField(max_length=40)
    url = models.FileField(upload_to=UPLOADS_DIR)
    hash = models.CharField(max_length=30)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name