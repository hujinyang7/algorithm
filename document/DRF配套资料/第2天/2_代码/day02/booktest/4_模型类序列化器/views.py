

"""==============1, 使用模型类序列化器, 测试序列化 ========================"""""
"""
1, 模型类中添加mobile字段
2, 删除序列化器中的mobile
3, 动态添加一mobile属性
4, 将mobile字段设置为write_only(只写,只进行反序列化)
"""
from booktest.models import BookInfo
from booktest.serializer import BookModelSerializer

#1,获取模型类对象
book = BookInfo.objects.get(id=1)
# book.mobile = "13838389438"

#2,创建序列化器对象
serializer = BookModelSerializer(instance=book)

#3,输出结果
serializer.data

"""==============2, 使用模型类序列化器, 测试反序列化, 入库操作========================"""""
from booktest.serializer import BookModelSerializer

#1,准备字典数据
book_dict = {
    "btitle":"鹿鼎记1",
    "bpub_date":"1999-01-01",
    "bread":10,
    "bcomment":5
}

#2,序列化器对象创建
serializer = BookModelSerializer(data=book_dict)

#3,校验,入库
serializer.is_valid(raise_exception=True)
serializer.save()

"""==============3, 使用模型类序列化器, 测试反序列化, 更新操作========================"""""
from booktest.serializer import BookModelSerializer
from booktest.models import BookInfo

#1,准备字典数据, 书籍对象
book = BookInfo.objects.get(id=9)
book_dict = {
    "btitle":"鹿鼎记2",
    "bpub_date":"1999-01-01",
    "bread":100,
    "bcomment":5
}

#2,序列化器对象创建
serializer = BookModelSerializer(instance=book,data=book_dict)

#3,校验,入库
serializer.is_valid(raise_exception=True)
serializer.save()



