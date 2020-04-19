from core.models import Project, Task
from rest_framework import serializers

from auth_.serializers import UserSerializer


class ProjectSerializer(serializers.ModelSerializer):
    creator_name = serializers.SerializerMethodField()
    creator_id = serializers.IntegerField(write_only=True)
    tasks_count = serializers.IntegerField(default=0)

    class Meta:
        model = Project
        fields = ('id', 'name', 'desc', 'creator_name', 'creator_id', 'tasks_count')


class TaskSerializer(serializers.ModelSerializer):
    project_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Task
        fields = ('id', 'name', 'document', 'status', 'is_deleted', 'project_id', 'executor', 'creator', 'priority','description')








