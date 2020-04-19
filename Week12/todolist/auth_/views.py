import logging

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer
from .models import MyUser

logger = logging.getLogger('log')

class RegisterUserAPIView(APIView):
    http_method_names = ['post']

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            Response(serializer.data)
            logger.info(f"{self.request.user} registered into the system")
            logger.warning(f"{self.request.user} registered into the system")
            logger.error(f"{self.request.user} registered into the system")
            logger.critical(f"{self.request.user} registered into the system")

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    # permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return MyUser.objects.all()

    @action(methods=['GET'], detail=False)
    def me(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)