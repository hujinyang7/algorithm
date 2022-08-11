from rest_framework.views import exception_handler
from rest_framework.response import Response
from django.db import DatabaseError

def custom_exception_handler(exc, context):

    #1,调用系统方法,处理了APIException的异常,或者其子类异常
    response = exception_handler(exc, context)

    #2,判断response是否有值
    if response is not None:
        response.data['status_code'] = response.status_code
    else:
        if isinstance(exc, DatabaseError):
            response = Response("数据库大出血")
        else:
            response = Response("其他异常!")

    return response