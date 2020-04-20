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
from core.serializers import ProjectSerializer, TaskFullSerializer, TaskShortSerializer, TaskChangeSerializer

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
                     # mixins.RetrieveModelMixin,
                     # mixins.UpdateModelMixin,
                     # mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    # permission_classes = (IsAuthenticated,)
    parser_classes = (FormParser, MultiPartParser, JSONParser)

    # def get_queryset(self):
    #     return Project.objects.for_user(user=self.request.user)

    @action(methods=['GET'], detail=False)
    def myprojects(self, request):
        projects = Project.objects.filter(creator=self.request.user)
        serializer = self.get_serializer(projects, many=True)
        return Response(serializer.data)

    @action(methods=['GET'], detail=True)
    def tasks(self, request, pk):
        instance = self.get_object()
        serializer = TaskShortSerializer(instance.tasks, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
        logger.info(f"{self.request.user} created task: {serializer.data.get('name')}")
        logger.warning(f"{self.request.user} created task: {serializer.data.get('name')}")
        logger.error(f"{self.request.user} created task: {serializer.data.get('name')}")
        logger.critical(f"{self.request.user} created task: {serializer.data.get('name')}")


class TaskViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    # serializer_class = TaskSerializer
    queryset = Task.objects.all()
    # permission_classes = (IsAuthenticated,)
    parser_classes = (FormParser, MultiPartParser, JSONParser)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return TaskFullSerializer
        if self.action == 'set_executor':
            return TaskShortSerializer
        if self.action in ['create', 'update']:
            return TaskChangeSerializer

    # def get_queryset(self):
    #     return Task.objects.for_user(user=self.request.user)

    # @action(methods=['PUT'], detail=True)
    # def set_executor(self, request, pk):
    #     instance = self.get_object()
    #     instance.set_executor(request.data.get('executor_id'))
    #     serializer = self.get_serializer(instance)
    #     logger.info(f"{self.request.user} set as executor id: {request.data.get('executor_id')}")
    #     return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
        logger.info(f"{self.request.user} created task: {serializer.data.get('name')}")
        logger.warning(f"{self.request.user} created task: {serializer.data.get('name')}")
        logger.error(f"{self.request.user} created task: {serializer.data.get('name')}")
        logger.critical(f"{self.request.user} created task: {serializer.data.get('name')}")







