from django.shortcuts import render
from django.views import View
from django import http
from booktest.models import BookInfo
import json

#1, 获取所有书籍,创建单本书籍 (列表视图)
class BookInfoView(View):

    def get(self,request):
        #1,查询所有的书籍
        books = BookInfo.objects.all()

        #2,将对象列表转成字典列表
        books_list = []
        for book in books:
            book_dict = {
                "btitle":book.btitle,
                "bpub_date":book.bpub_date,
                "bread":book.bread,
                "bcomment":book.bcomment
            }
            books_list.append(book_dict)

        #3,返回响应, safe=False允许非字典数据可以被返回
        return http.JsonResponse(books_list,safe=False)


    def post(self,request):
        #1,获取参数
        data_dict = json.loads(request.body.decode())
        # btitle = data_dict["btitle"]
        # bpub_date = data_dict["bpub_date"]
        # bread = data_dict["bread"]
        # bcomment = data_dict["bcomment"]

        #2,校验参数(省略)

        #3,数据入库
        # book = BookInfo.objects.create(
        #     btitle=btitle,
        #     bpub_date=bpub_date,
        #     bread=bread,
        #     bcomment=bcomment
        # )

        book = BookInfo.objects.create(**data_dict)

        book_dict = {
            "btitle": book.btitle,
            "bpub_date": book.bpub_date,
            "bread": book.bread,
            "bcomment": book.bcomment
        }

        #4,返回响应
        return http.JsonResponse(book_dict,status=201)

#2, 获取单个书籍,修改单本书籍,删除单本书籍 (详情视图)
class BookInfoDetailView(View):
    def get(self,request,book_id):

        #1,获取书籍
        book = BookInfo.objects.get(id=book_id)

        #2,校验数据(省略)

        #3,将书籍转成字典数据
        book_dict = {
            "btitle": book.btitle,
            "bpub_date": book.bpub_date,
            "bread": book.bread,
            "bcomment": book.bcomment
        }

        #4,返回响应
        return http.JsonResponse(book_dict,status=200)

    def put(self,request,book_id):

        #1,获取数据,获取对象
        data_dict = json.loads(request.body.decode())
        # book = BookInfo.objects.get(id=book_id)

        #2,数据校验(省略)

        #3,数据入库
        BookInfo.objects.filter(id=book_id).update(**data_dict)
        book = BookInfo.objects.get(id=book_id)

        book_dict = {
            "btitle": book.btitle,
            "bpub_date": book.bpub_date,
            "bread": book.bread,
            "bcomment": book.bcomment
        }
        #4,返回响应
        return http.JsonResponse(book_dict, status=201)

    def delete(self,request,book_id):

        #1,删除书籍
        BookInfo.objects.get(id=book_id).delete()

        #2,返回响应
        return http.HttpResponse(status=204)