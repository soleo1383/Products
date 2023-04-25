from rest_framework import serializers
from .models import Category, File, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'description', 'avatar']


class FileSerializer(serializers.ModelSerializer):
    file_type = serializers.SerializerMethodField()

    class Meta:
        model = File
        fields = ['id', 'file_type', 'title', 'file']

    def get_file_type(self, obj):
        return obj.get_file_type_display()


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    categories = CategorySerializer(many=True)
    files = FileSerializer(many=True)
    #foo = serializers.SerializerMethodField()

    class Meta:

        model = Product
        fields = ['id', 'title', 'description', 'avatar', 'categories', 'files']

    #def get_foo(self, obj):
    #   return obj.id
