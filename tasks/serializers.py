from rest_framework import serializers
from .models import Task, Tag


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ('name', 'date_of_creation', 'task')


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ('name',  'description', 'date_of_creation', 'tags')







