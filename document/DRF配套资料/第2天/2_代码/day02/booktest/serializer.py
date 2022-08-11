from rest_framework import serializers
from booktest.models import BookInfo

#1,定义书籍模型类序列化器
class BookInfoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookInfo
        fields = "__all__"