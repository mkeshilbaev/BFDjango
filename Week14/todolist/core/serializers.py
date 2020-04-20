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
        fields = ('id', 'name', 'document', 'status', 'is_deleted', 'project_id', 'executor', 'creator', 'priority', 'description')


class TaskShortSerializer(serializers.ModelSerializer):
    is_deleted = serializers.BooleanField(read_only=True)
    project_id = serializers.IntegerField(write_only=True)
    executor = UserSerializer(read_only=True)
    creator = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Task
        fields = ('id', 'name', 'document', 'status', 'is_deleted', 'project_id', 'executor', 'creator')
        # read_only_fields = ('is_deleted', 'executor')
        # write_only_fields = ('project_id', 'executor')
        # exclude = ('name',)
        # fields = ('__all__')


class TaskFullSerializer(TaskShortSerializer):
    class Meta(TaskShortSerializer.Meta):
        fields = TaskShortSerializer.Meta.fields + ('priority', 'description',)


class TaskChangeSerializer(TaskShortSerializer):
    pass





