import logging

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser

from core.models import Project, Task
from core.serializers import ProjectSerializer, TaskSerializer

logger = logging.getLogger('log')


class ProjectListAPIView(mixins.ListModelMixin,
                         mixins.CreateModelMixin,
                         generics.GenericAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ProjectViewSet(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    # permission_classes = (IsAuthenticated,)
    parser_classes = (FormParser, MultiPartParser, JSONParser)

    # def get_queryset(self):
    #     return Project.objects.for_user(user=self.request.user)

    @action(methods=['GET'], detail=False)
    def projects(self, request):
        projects = Project.objects.filter(creator=self.request.user)
        serializer = self.get_serializer(projects, many=True)
        return Response(serializer.data)

    @action(methods=['GET'], detail=True)
    def tasks(self, request, pk):
        instance = self.get_object()
        serializer = TaskSerializer(instance.tasks, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
        logger.info(f"{self.request.user} created task: {serializer.data.get('name')}")
        logger.warning(f"{self.request.user} created task: {serializer.data.get('name')}")
        logger.error(f"{self.request.user} created task: {serializer.data.get('name')}")
        logger.critical(f"{self.request.user} created task: {serializer.data.get('name')}")


class TaskViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    # permission_classes = (IsAuthenticated,)
    parser_classes = (FormParser, MultiPartParser, JSONParser)

    def get_queryset(self):
        return Task.objects.for_user(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
        logger.info(f"{self.request.user} created task: {serializer.data.get('name')}")
        logger.warning(f"{self.request.user} created task: {serializer.data.get('name')}")
        logger.error(f"{self.request.user} created task: {serializer.data.get('name')}")
        logger.critical(f"{self.request.user} created task: {serializer.data.get('name')}")







