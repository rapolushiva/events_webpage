from django.db import models
from datetime  import datetime
class Locations(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

# Create your models here.
class event(models.Model):
    event_name=models.CharField(max_length=100, null=False, blank=False)
    data=models.CharField(max_length=200, null=False, blank=False)
    time=models.DateTimeField(default=datetime.now, blank=True)
    location=models.ForeignKey(Locations, on_delete=models.CASCADE, null=False, default=True)
    image=models.ImageField(null=False, blank=False)
    is_liked=models.BooleanField(default=False)
    user_id=models.CharField(max_length=100, null=False, blank=False)
    def __str__(self):
        return self.event_name










# Create your models here.