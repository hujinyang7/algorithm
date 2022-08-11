from collections import OrderedDict

from django.shortcuts import render
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet
from booktest.models import BookInfo
from booktest.serializers import BookInfoModelSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.throttling import AnonRateThrottle
from rest_framework.views import APIView
from rest_framework.pagination import LimitOffsetPagination,PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import APIException,ValidationError
from django.db import DatabaseError

#自定义分页对象
class MyPageNumberPagination(PageNumberPagination):
    #1,默认的大小
    page_size = 3

    #2,前端可以指定页面大小
    page_size_query_param = 'page_size'

    #3,页面的最大大小
    max_page_size = 5

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('haha', 'zhangsan'),
            ('count', self.page.paginator.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data)
        ]))


#1,视图集
class BookInfoModelViewSet(ModelViewSet):
    """
    list:
        获取所有数据

    create:
        创建单个对象

    """

    queryset = BookInfo.objects.all()
    serializer_class = BookInfoModelSerializer

    #1,局部认证
    # authentication_classes = [SessionAuthentication]

    #2,局部权限
    # permission_classes = [AllowAny]

    #3,局部限流
    # throttle_classes = [AnonRateThrottle]

    #4,可选限流
    # throttle_scope = 'downloads'

    #5,局部分页
    # pagination_class = LimitOffsetPagination # ?limit=100 或者 ?offset=400&limit=100
    # pagination_class = PageNumberPagination # ?page=4

    #6,自定义分页对象
    pagination_class = MyPageNumberPagination # ?page=4 或者 ?page=4&page_size=100

    #7,局部过滤
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['id', 'btitle',"is_delete"]

    #8,局部排序
    # filter_backends = [filters.OrderingFilter] # 导包路径: from rest_framework import filters
    # ordering_fields = ['id', 'btitle','bread'] #查询格式: ?ordering=-bread,id


    #1,获取阅读量大于20的书籍
    @action(methods=['GET'],detail=False) #生成路由规则: 前缀/方法名/
    def bread_book(self,request):
        #1,获取指定书籍
        books = BookInfo.objects.filter(bread__gt=20)

        #2,创建序列化器对象
        serializer = self.get_serializer(instance=books,many=True)

        #3,返回响应
        return Response(serializer.data)

    #2,修改书籍编号为1的, 阅读量为99
    @action(methods=["PUT"],detail=True) #生成路由规则: 前缀/{pk}/方法名/
    def update_book_bread(self,request,pk):
        #1,获取参数
        book = self.get_object()
        data = request.data

        #2,创建序列化器
        serializer = self.get_serializer(instance=book,data=data,partial=True)

        #3,校验,入库
        serializer.is_valid(raise_exception=True)
        serializer.save()

        #4,返回响应
        return Response(serializer.data,status=201)

class TestView(APIView):
    # throttle_scope = "uploads"
    def get(self,request):

        # raise DatabaseError("DatabaseError!!!")
        # raise Exception("报错了!!!")
        raise APIException("APIException!!!")
        # raise ValidationError("ValidationError!!!")

        return Response("testing....")

