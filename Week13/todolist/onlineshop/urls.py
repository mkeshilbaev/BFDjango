from django.urls import path
from rest_framework.routers import DefaultRouter

from onlineshop import views
# from core.views import ProductListViewSet, CategoryListApiView

urlpatterns = [
    # path('categories/', views.CategoryListApiView.as_view()),
    # path('products/', views.ProductListApiView.as_view()),
    path('categories/', views.CategoryList.as_view()),
    path('categories/<int:pk>/', views.CategoryDetail.as_view()),
    path('categories/<int:pk>/products/', views.CategoryProductList.as_view())
]

# router = DefaultRouter()
# router.register('products', ProductListViewSet, basename='core')
# urlpatterns += router.urls