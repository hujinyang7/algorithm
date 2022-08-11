from rest_framework.views import APIView
from django import http
from rest_framework.response import Response
from rest_framework import status
from booktest.models import BookInfo
from booktest.serializer import BookInfoModelSerializer
from rest_framework.generics import GenericAPIView

#1,定义类,集成APIView
class BookAPIView(APIView):

    def get(self,request):
        """
        View获取数据方式:
            GET:
                request.GET
            POST:
                request.POST
                request.body

        APIView获取数据方式
            GET:
                reqeust.query_params
            POST:
                request.data

        :param request:
        :return:
        """
        #1,获取APIVIew中的get请求参数
        # print(request.query_params)

        return Response([{"name":"zhangsan"},{"age":13}],status=status.HTTP_404_NOT_FOUND)

    def post(self,request):

        # 2,获取APIView中的post的参数
        print(request.data)

        return http.HttpResponse("post")

#2,序列化器和APIView实现列表视图
class BookListAPIView(APIView):

    def get(self,request):
        #1,查询所有的书籍
        books = BookInfo.objects.all()

        #2,将对象列表转成字典列表
        serializr = BookInfoModelSerializer(instance=books,many=True)

        #3,返回响应
        return Response(serializr.data)


    def post(self,request):
        #1,获取参数
        data_dict = request.data

        #2,创建序列化器
        serializer = BookInfoModelSerializer(data=data_dict)

        #3,校验,入库
        serializer.is_valid(raise_exception=True)
        serializer.save()

        #4,返回响应
        return Response(serializer.data,status=status.HTTP_201_CREATED)

#3,序列化器和APIView实现详情视图
class BookDetailAPIView(APIView):
    def get(self,request,book_id):

        #1,获取书籍
        book = BookInfo.objects.get(id=book_id)

        #2,创建序列化器对象
        serializer = BookInfoModelSerializer(instance=book)

        #4,返回响应
        return Response(serializer.data,status=status.HTTP_200_OK)

    def put(self,request,book_id):

        #1,获取数据,获取对象
        data_dict = request.data
        book = BookInfo.objects.get(id=book_id)

        #2,创建序列化器对象
        serializer = BookInfoModelSerializer(instance=book,data=data_dict)

        #3,校验,入库
        serializer.is_valid(raise_exception=True)
        serializer.save()

        #4,返回响应
        return Response(serializer.data,status=status.HTTP_201_CREATED)

    def delete(self,request,book_id):

        #1,删除书籍
        BookInfo.objects.get(id=book_id).delete()

        #2,返回响应
        return Response(status=status.HTTP_204_NO_CONTENT)

#4,二级视图GenericAPIView特点
"""
特点: 
1, GenericAPIView,继承自APIView类，为列表视图, 和详情视图,添加了常用的行为和属性。
    行为(方法)
        get_queryset:  获取queryset的数据集
        get_serializer: 获取serializer_class序列化器对象
        get_object:    根据lookup_field获取单个对象
    
    属性
        queryset:   通用的数据集
        serializer_class: 通用的序列化器
        lookup_field:   默认是pk,可以手动修改id

2, 可以和一个或多个mixin类配合使用。

"""

#5,使用二级视图GenericAPIView实现, 列表视图
class BookListGenericAPIView(GenericAPIView):

    #1,提供公共的属性
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoModelSerializer


    def get(self,request):
        #1,查询所有的书籍
        # books = self.queryset
        books = self.get_queryset()

        #2,将对象列表转成字典列表
        # serializr = BookInfoModelSerializer(instance=books,many=True)
        # serializr = self.serializer_class(instance=books,many=True)
        # serializr = self.get_serializer_class()(instance=books,many=True)
        serializr = self.get_serializer(instance=books,many=True)

        #3,返回响应
        return Response(serializr.data)


    def post(self,request):
        #1,获取参数
        data_dict = request.data

        #2,创建序列化器
        # serializer = BookInfoModelSerializer(data=data_dict)
        serializer = self.get_serializer(data=data_dict)

        #3,校验,入库
        serializer.is_valid(raise_exception=True)
        serializer.save()

        #4,返回响应
        return Response(serializer.data,status=status.HTTP_201_CREATED)

#6,使用二级视图GenericAPIView实现, 详情视图
class BookDetailGenericAPIView(GenericAPIView):

    #1,提供通用属性
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoModelSerializer
    # lookup_field = "id"
    lookup_url_kwarg = "book_id"

    def get(self,request,book_id):

        #1,获取书籍
        # book = BookInfo.objects.get(id=book_id)
        book = self.get_object() #根据id到queryset中取出书籍对象

        #2,创建序列化器对象
        serializer = self.get_serializer(instance=book)

        #4,返回响应
        return Response(serializer.data,status=status.HTTP_200_OK)

    def put(self,request,book_id):

        #1,获取数据,获取对象
        data_dict = request.data
        book = self.get_object()

        #2,创建序列化器对象
        serializer = self.get_serializer(instance=book,data=data_dict)

        #3,校验,入库
        serializer.is_valid(raise_exception=True)
        serializer.save()

        #4,返回响应
        return Response(serializer.data,status=status.HTTP_201_CREATED)

    def delete(self,request,book_id):

        #1,删除书籍
        self.get_object().delete()

        #2,返回响应
        return Response(status=status.HTTP_204_NO_CONTENT)

#7,Mixin
"""
Mixin,特点: 
1, mixin类提供用于提供基本视图行为(列表视图, 详情视图)的操作
2, 配合二级视图GenericAPIView使用的

类名称                 提供方法        功能
ListModelMixin        list          查询所有的数据
CreateModelMixin      create        创建单个对象
RetrieveModelMixin    retrieve      获取单个对象
UpdateModelMixin      update        更新单个对象
DestroyModelMixin     destroy       删除单个对象

"""

from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
#8,mixin和二级视图GenericAPIView, 实现列表视图, 详情视图
class BookListMixinGenericAPIView(GenericAPIView,ListModelMixin,CreateModelMixin):

    #1,提供公共的属性
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoModelSerializer

    def get(self,request):
        return self.list(request)


    def post(self,request):
        return self.create(request)


class BookDetailMixinGenericAPIView(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):

    #1,提供通用属性
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoModelSerializer
    # lookup_field = "id"
    lookup_url_kwarg = "book_id"

    def get(self,request,book_id):
        return self.retrieve(request)

    def put(self,request,book_id):
        return self.update(request)

    def delete(self,request,book_id):
        return self.destroy(request)

#9,三级视图
"""
特点:
如果没有大量自定义的行为, 可以使用通用视图(三级视图)解决

常见的三级视图:
类名称                 父类              提供方法        作用
CreateAPIView       GenericAPIView，   post           创建单个对象
                    CreateModelMixin
                    
ListAPIView         GenericAPIView,    get            查询所有的数据
                    ListModelMixin

RetrieveAPIView     GenericAPIView,    get            获取单个对象
                    RetrieveModelMixin 
                    
DestroyAPIView      GenericAPIView,    delete         删除单个对象
                    DestroyModelMixin
                    
UpdateAPIView       GenericAPIView,    put            更新单个对象
                    UpdateModelMixin             


"""

#10,三级视图,实现列表,详情视图
from rest_framework.generics import ListAPIView,CreateAPIView
class BookListThirdView(ListAPIView,CreateAPIView):

    #1,提供公共的属性
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoModelSerializer

from rest_framework.generics import RetrieveAPIView,UpdateAPIView,DestroyAPIView
class BookDetailThirdView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):

    #1,提供通用属性
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoModelSerializer


#11, 视图集
from rest_framework.viewsets import GenericViewSet,ModelViewSet,ReadOnlyModelViewSet
"""
视图集
特点:
    1,可以将一组相关的操作, 放在一个类中进行完成
    2,不提供get,post方法, 使用retrieve, create方法来替代
    3,可以将标准的请求方式(get,post,put,delete), 和mixin中的方法做映射
    
常见的视图集:
类名称                 父类              作用
ViewSet               APIView          可以做路由映射
                      ViewSetMixin
                      
GenericViewSet        GenericAPIView   可以做路由映射,可以使用三个属性,三个方法
                      ViewSetMixin
                             
ModelViewSet          GenericAPIView   所有的增删改查功能,可以使用三个属性,三个方法
                      5个mixin类

ReadOnlyModelViewSet  GenericAPIView   获取单个,所有数据,可以使用三个属性,三个方法
                      RetrieveModelMixin
                      ListModelMixin

"""

#12, 使用viewset实现获取所有和单个
from django.shortcuts import get_object_or_404
from booktest.serializer import BookInfoModelSerializer
from rest_framework import viewsets

class BooksViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving books.
    """
    def list(self, request):
        queryset = BookInfo.objects.all()
        serializer = BookInfoModelSerializer(instance=queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = BookInfo.objects.all()
        book = get_object_or_404(queryset, pk=pk)
        serializer = BookInfoModelSerializer(instance=book)
        return Response(serializer.data)

#13,使用ReadOnlyModelViewSet实现获取单个和所有
from rest_framework.viewsets import ReadOnlyModelViewSet
class BooksReadOnlyModelViewSet(ReadOnlyModelViewSet):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoModelSerializer


#14,ModelViewSet实现列表视图,详情视图功能
from rest_framework.viewsets import ModelViewSet
class BookModelViewSet(ModelViewSet):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoModelSerializer
