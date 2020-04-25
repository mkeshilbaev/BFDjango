from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

from recruting.main import views
from recruting.main.views import UserViewSet

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('reg/', views.RegistrationView.as_view()),
    # path('change_password/', views.PasswordView.as_view()),
]

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')

urlpatterns += router.urls