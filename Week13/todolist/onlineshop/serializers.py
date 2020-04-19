from rest_framework import serializers

from onlineshop.models import Category, Product


# class CategorySerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(required=True)
#     desc = serializers.CharField(required=True)
#
#     def create(self, validated_data):
#         category = Category(**validated_data)
#         category.save()
#         return category
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.save()
#         return instance

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