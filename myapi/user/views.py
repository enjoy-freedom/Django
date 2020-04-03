
from django.contrib.auth.models import User
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from authTest.models import App


@swagger_auto_schema(
    method="post",
    request_body=openapi.Schema(
        title='xxx',
        type=openapi.TYPE_STRING,
        description="创建新用户",
        example="""
                {
                "username":"test",
                "password":"test",
                "email":"657176019@qq.com"
                }
            """
    ))
@api_view(['POST'])
def creat_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')
    user = App.objects.filter(username=username)
    if user:
        return Response({"code": 0,
                             "msg": "创建用户失败,该用户名已存在!"},status=status.HTTP_400_BAD_REQUEST)
    new_user = App.objects.create_user(username=username, password=password, email=email)
    if new_user:
        return Response({"code": 0,
                             "msg": "创建用户成功!"}, status=status.HTTP_201_CREATED)
    else:
        return Response({"code": 0,
                             "msg": "创建用户失败!"}, status=status.HTTP_400_BAD_REQUEST)
# def creat_user(request):
#     username = request.data.get('username')
#     password = request.data.get('password')
#     email = request.data.get('email')
#     user = User.objects.filter(username=username)
#     if user:
#         return Response({"code": 0,
#                              "msg": "创建用户失败,该用户名已存在!"},status=status.HTTP_400_BAD_REQUEST)
#
    # new_user = User.objects.create_user(username=username, password=password, email=email)
#     if new_user:
#         return Response({"code": 0,
#                              "msg": "创建用户成功!"}, status=status.HTTP_201_CREATED)
#     else:
#         return Response({"code": 0,
#                              "msg": "创建用户失败!"}, status=status.HTTP_400_BAD_REQUEST)
