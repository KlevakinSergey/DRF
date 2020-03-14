from django.db import models
from django.urls import reverse




# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=50)
    date_of_creation = models.DateTimeField(auto_now_add=True, null=True)
    task = models.ManyToManyField('Task', related_name='tags', blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tag-detail', kwargs={'pk': self.pk})


class Task(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    description = models.TextField(blank=True, null=True)
    date_of_creation = models.DateTimeField(auto_now_add=True)
    tag = models.ManyToManyField(Tag, blank=True, related_name='tasks')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('task-detail', kwargs={'pk': self.pk})
