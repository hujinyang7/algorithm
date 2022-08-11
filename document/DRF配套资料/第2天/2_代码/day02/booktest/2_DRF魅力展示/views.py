from rest_framework import serializers
from booktest.models import BookInfo
from rest_framework.viewsets import ModelViewSet

#2,序列化器
class BookModelSeriralizer(serializers.ModelSerializer):
    class Meta:
        model = BookInfo
        fields = "__all__"

#3,视图集
class BookViewSet(ModelViewSet):
    queryset = BookInfo.objects.all()
    serializer_class = BookModelSeriralizer