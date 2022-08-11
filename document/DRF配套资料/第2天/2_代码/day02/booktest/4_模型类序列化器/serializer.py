from rest_framework import serializers
from booktest.models import BookInfo

#1,定义书籍模型类序列化器
class BookModelSerializer(serializers.ModelSerializer):

    mobile = serializers.CharField(max_length=11,min_length=11,label="手机号",write_only=True)

    class Meta:
        model = BookInfo #参考模型类生成字段
        fields = "__all__" #生成所有字段

        #1,生成指定的字段
        # fields = ["id","btitle","bpub_date","mobile"]

        #2,设置只读字段
        # read_only_fields = ["btitle","bpub_date"]

        #3,给生成的字段添加额外约束
        extra_kwargs = {
            "bread":{
                "max_value":999999,
                "min_value":0
            },
            "bcomment": {
                "max_value": 888888,
                "min_value": 0
            }
        }