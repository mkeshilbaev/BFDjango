from rest_framework import mixins, generics, viewsets
from core.models import Category, Product
from core.serializers import CategorySerializer, ProductFullSerializer
from core.serializers import ProductShortSerializer
from django.http import Http404


class CategoryList(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    # permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Category.objects.for_user(self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryProductList(generics.ListCreateAPIView):
    serializer_class = ProductFullSerializer
    search_fields = ('name', 'price', 'count')
    ordering_fields = ('name', 'price')
    ordering = ('price',)

    def get_queryset(self):
        try:
            category = Category.objects.get(id=self.kwargs.get('pk'))
        except Category.DoesNotExist:
            raise Http404
        queryset = category.products.all()
        return queryset



# class CategoryListApiView(mixins.ListModelMixin,
#                           mixins.CreateModelMixin,
#                           generics.GenericAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#     # permission_classes = ()
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#
# class CategoryDetailApiView(mixins.RetrieveModelMixin,
#                             mixins.UpdateModelMixin,
#                             mixins.DestroyModelMixin,
#                             generics.GenericAPIView):
#
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#     # permission_classes = ()
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
#
#
# class ProductListApiView(mixins.ListModelMixin,
#                          mixins.CreateModelMixin,
#                          generics.GenericAPIView):
#     def get_queryset(self):
#         try:
#             category = Category.objects.get(id=self.kwargs.get('pk'))
#             return category.products.all()
#         except Category.DoesNotExist:
#             return Http404
#     serializer_class = ProductShortSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#
# class ProductListViewSet(mixins.ListModelMixin,
#                          mixins.CreateModelMixin,
#                          mixins.RetrieveModelMixin,
#                          mixins.UpdateModelMixin,
#                          mixins.DestroyModelMixin,
#                          viewsets.GenericViewSet):
#     queryset = Product.objects.all()
#
#     def get_serializer_class(self):
#         if self.action == 'list':
#             return ProductShortSerializer
#         if self.action == 'retrieve':
#             return ProductFullSerializer
#         return ProductShortSerializer




