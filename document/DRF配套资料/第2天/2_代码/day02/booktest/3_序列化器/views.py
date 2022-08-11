
""" ===============1, 序列化器,序列化单个对象 ================= """""
from booktest.models import BookInfo
from booktest.serializer import BookSerializer

#1,获取书籍对象
book = BookInfo.objects.get(id=1)

#2,创建序列化器对象, instance=book 表示将哪一本数据进行序列化
serializer = BookSerializer(instance=book)

#3,输出序列化之后的结果
serializer.data
"""
{'id': 1, 'btitle': '射雕英雄传', 'bpub_date': '1980-05-01', 'bread': 12, 'bcomment': 34, 'is_delete': False}
"""

""" ===============2, 序列化器,序列化列表数据 ================= """""
from booktest.models import BookInfo
from booktest.serializer import BookSerializer

#1,查询所有的书籍
books = BookInfo.objects.all()

#2,创建序列化器对象,many=True 表示传入的是列表对象(多个数据)
serializer = BookSerializer(instance=books,many=True)

#3,输出序列化的结果
serializer.data
"""
[
OrderedDict([('id', 1), ('btitle', '射雕英雄传'), ('bpub_date', '1980-05-01'), ('bread', 12), ('bcomment', 34), ('is_delete', False)]), 
OrderedDict([('id' ('btitle', '天龙八部'), ('bpub_date', '1986-07-24'), ('bread', 36), ('bcomment', 40), ('is_delete', False)]), 
OrderedDict([('id', 3), ('btitle', '笑傲江湖'), ('bp, '1995-12-24'), ('bread', 20), ('bcomment', 80), ('is_delete', False)]), 
OrderedDict([('id', 4), ('btitle', '雪山飞狐'), ('bpub_date', '1987-11-11'), ('bread', 58'bcomment', 24), ('is_delete', False)]), 
OrderedDict([('id', 6), ('btitle', '金瓶x2'), ('bpub_date', '2019-01-01'), ('bread', 10), ('bcomment', 5), ('is_delete', Fse)])
]
"""

""" ===============3, 英雄序列化器, 关联外键 ================= """""
from booktest.models import HeroInfo
from booktest.serializer import HeroInfoSerializer

#1,获取单个英雄
hero = HeroInfo.objects.get(id=1)

#2,创建英雄序列化器
serializer = HeroInfoSerializer(instance=hero)

#3,输出结果
serializer.data


""" ===============4, 反序列化-字段类型校验 ================= """""
from booktest.serializer import BookSerializer

#1,准备字典数据
data_dict = {
    "btitle":"金瓶x-插画版",
    "bpub_date":"2019-01-01",
    "bread":15,
    "bcomment":25
}

#2,创建序列化器对象
serializer = BookSerializer(data=data_dict)

#3,校验
# serializer.is_valid()
serializer.is_valid(raise_exception=True)


""" ===============5, 反序列化-字段选项校验 ================= """""
from booktest.serializer import BookSerializer

#1,准备字典数据
data_dict = {
    "btitle":"金瓶x",
    "bpub_date":"2019-01-01",
    "bread":15,
    "bcomment":99
}

#2,创建序列化器对象
serializer = BookSerializer(data=data_dict)

#3,校验
# serializer.is_valid()
serializer.is_valid(raise_exception=True)


""" ===============6, 反序列化-单字段校验 ================= """""
from booktest.serializer import BookSerializer

#1,准备字典数据
data_dict = {
    "btitle":"金瓶x",
    "bpub_date":"2019-01-01",
    "bread":15,
    "bcomment":5
}

#2,创建序列化器对象
serializer = BookSerializer(data=data_dict)

#3,校验
# serializer.is_valid()
serializer.is_valid(raise_exception=True)

""" ===============7, 反序列化-多字段校验 ================= """""
from booktest.serializer import BookSerializer

#1,准备字典数据
data_dict = {
    "btitle":"金瓶xxx",
    "bpub_date":"2019-01-01",
    "bread":33,
    "bcomment":22
}

#2,创建序列化器对象
serializer = BookSerializer(data=data_dict)

#3,校验
# serializer.is_valid()
serializer.is_valid(raise_exception=True)


""" ===============8, 反序列化-自定义校验 ================= """""
from booktest.serializer import BookSerializer

#1,准备字典数据
data_dict = {
    "btitle":"金瓶xxx",
    "bpub_date":"2011-11-01",
    "bread":11,
    "bcomment":5
}

#2,创建序列化器对象
serializer = BookSerializer(data=data_dict)

#3,校验
# serializer.is_valid()
serializer.is_valid(raise_exception=True)

""" ===============9, 反序列化-数据入库,create ================= """""
from booktest.serializer import BookSerializer

#1,准备字典数据
data_dict = {
    "btitle":"金瓶xxx-精装版",
    "bpub_date":"2015-11-01",
    "bread":11,
    "bcomment":5
}

#2,创建序列化器对象
serializer = BookSerializer(data=data_dict)

#3,校验
# serializer.is_valid()
serializer.is_valid(raise_exception=True)

#4,入库
serializer.save()

""" ===============10, 反序列化-数据更新update ================= """""
from booktest.serializer import BookSerializer
from booktest.models import BookInfo

#1,准备字典数据
book = BookInfo.objects.get(id=8)
data_dict = {
    "btitle":"金瓶xxx-连环画",
    "bpub_date":"2019-11-11",
    "bread":30,
    "bcomment":20
}

#2,创建序列化器对象
serializer = BookSerializer(instance=book,data=data_dict)

#3,校验
# serializer.is_valid()
serializer.is_valid(raise_exception=True)

#4,入库
serializer.save()

