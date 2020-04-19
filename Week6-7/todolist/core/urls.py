from django.urls import path
from core.views import ProjectViewSet, TaskViewSet
from rest_framework import routers
from core.views import ProjectListAPIView


urlpatterns = [
    # path('projects/', ProjectListAPIView.as_view())
]

router = routers.DefaultRouter()
router.register('projects', ProjectViewSet, basename='core')
router.register('tasks', TaskViewSet, basename='core')

urlpatterns = router.urls