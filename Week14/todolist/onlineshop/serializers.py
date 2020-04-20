from rest_framework import serializers

from onlineshop.models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    attachment = serializers.FileField()
    class Meta:
        model = Product
        fields = ('id', 'name', 'attachment')


class ProductShortSerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField(write_only=True)
    attachment = serializers.FileField()

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'count', 'category_id', 'attachment')

    def validate_count(self, count):
        if count < 0:
            raise serializers.ValidationError('no available product')


class ProductFullSerializer(ProductShortSerializer):
    category = CategorySerializer(read_only=True)

    class Meta(ProductShortSerializer.Meta):
        model = Product
        fields = ProductShortSerializer.Meta.fields + ('category',)