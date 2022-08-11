from rest_framework import serializers
from booktest.models import BookInfo
"""
定义序列化器:
1, 定义类, 继承自Serializer
2, 编写字段名称, 和模型类一样
3, 编写字段类型, 和模型类一样
4, 编写字段选项, 和模型类一样
    read_only: 只读
    label: 字段说明

序列化器作用:
1, 反序列化: 将json(dict)数据, 转成模型类对象
    ①: 校验
    ②: 入库
    
2, 序列化: 将模型类对象, 转成json(dict)数据


①: 校验
1, 字段类型校验
2, 字段选项校验
3, 单字段校验, 方法
4, 多字段校验, 方法
5, 自定义校验, 方法

"""""
#需求: 添加的书籍的日期不能小于2015年
def check_bpub_date(date):
    print("date = {}".format(date))

    if date.year < 2015:
        raise serializers.ValidationError("日期不能小于2015年")

    return date


#1,定义书籍序列化器
class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True,label="书籍编号")
    btitle = serializers.CharField(max_length=20,min_length=3,label="名称")
    bpub_date = serializers.DateField(label="发布日期",validators=[check_bpub_date])
    bread = serializers.IntegerField(default=0,min_value=0,label="阅读量")
    bcomment = serializers.IntegerField(default=0,max_value=50,label="评论量")
    is_delete = serializers.BooleanField(default=False,label="逻辑删除")

    #1,关联英雄字段, 在一方中,输出多方内容的时候加上many=True
    # heroinfo_set = serializers.PrimaryKeyRelatedField(read_only=True,many=True)
    heroinfo_set = serializers.StringRelatedField(read_only=True,many=True)

    #3, 单字段校验, 方法; 需求: 添加的书籍必须包含'金瓶'
    def validate_btitle(self, value):
        # print("value = {}".format(value))

        #1,判断传入的value中是否包含金瓶
        if "金瓶" not in value:
            raise serializers.ValidationError("书名必须包含金瓶")

        #2,返回结果
        return value

    #4,多字段校验, 方法; 添加书籍的时候,评论量不能大于阅读量
    def validate(self, attrs):
        """
        :param attrs: 外界传入的需要校验的字典
        :return:
        """
        #1,判断评论量和阅读量的关系
        if attrs["bread"] < attrs["bcomment"]:
            raise serializers.ValidationError("评论量不能大于阅读量")

        #2,返回结果
        return attrs

    #5,重写create方法,实现数据入库
    def create(self, validated_data):
        # print("validated_data = {}".format(validated_data))

        #1,创建book对象,入库
        book = BookInfo.objects.create(**validated_data)

        #2,返回响应
        return book

    #6,重写update方法,实现数据更新
    def update(self, instance, validated_data):
        """
        :param instance: 需要更新的对象
        :param validated_data: 验证成功之后的数据
        :return:
        """
        #1,更新数据
        instance.btitle = validated_data["btitle"]
        instance.bpub_date = validated_data["bpub_date"]
        instance.bread = validated_data["bread"]
        instance.bcomment = validated_data["bcomment"]
        instance.save()

        #2,返回数据
        book = BookInfo.objects.get(id=instance.id)
        return book


#2,定义英雄序列化器
class HeroInfoSerializer(serializers.Serializer):
    """英雄数据序列化器"""
    GENDER_CHOICES = (
        (0, 'male'),
        (1, 'female')
    )
    id = serializers.IntegerField(label='ID', read_only=True)
    hname = serializers.CharField(label='名字', max_length=20)
    hgender = serializers.ChoiceField(choices=GENDER_CHOICES, label='性别', required=False)
    hcomment = serializers.CharField(label='描述信息', max_length=200, required=False, allow_null=True)

    #1,添加外键,主键表示 必须提供`queryset` 选项, 或者设置 read_only=`True`.
    # hbook = serializers.PrimaryKeyRelatedField(queryset=BookInfo.objects.all())
    # hbook = serializers.PrimaryKeyRelatedField(read_only=True)

    #2,添加外键, 来自于关联模型类, __str__的返回值
    # hbook = serializers.StringRelatedField(read_only=True)

    #3,添加外键,关联另外一个序列化器
    hbook = BookSerializer(read_only=True)