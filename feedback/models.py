from django.db import models
import uuid

# Create your models here.
class Course(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    content_rate = models.IntegerField()
    class_rate = models.IntegerField()
    facilitator_rate = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    liked = models.BooleanField()
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING, null=True)

    def get_average(self):
        average = (self.content_rate + self.class_rate + self.facilitator_rate ) / 3
        return average
    
    def __str__(self):
        return f'{self.description}'


