from django.db import models

# Create your models here.

class Group(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
    
class Chat(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)
    time_stamp = models.DateTimeField(auto_now=True)
