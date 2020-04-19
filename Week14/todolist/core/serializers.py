from core.models import Project, Task
from rest_framework import serializers

from auth_.serializers import UserSerializer


class ProjectSerializer(serializers.ModelSerializer):
    creator_name = serializers.SerializerMethodField()
    # creator_id = serializers.IntegerField(write_only=True)
    tasks_count = serializers.IntegerField(default=0)
    attachment = serializers.FileField()

    class Meta:
        model = Project
        fields = ('id', 'name', 'desc', 'creator_name', 'tasks_count', 'attachment')


class TaskSerializer(serializers.ModelSerializer):
    project_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Task
        fields = ('id', 'name', 'document', 'status', 'is_deleted', 'project_id', 'creator', 'priority', 'description')








