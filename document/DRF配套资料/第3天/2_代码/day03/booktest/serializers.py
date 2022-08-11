from rest_framework import serializers
from booktest.models import BookInfo

#1,模型类序列化器
class BookInfoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookInfo
        fields = "__all__"

        extra_kwargs = {
            'bread':{
                'help_text':"书籍阅读量"
            }
        }