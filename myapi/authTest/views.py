

# Create your views here.
from django.http import JsonResponse
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from authTest.models import App


@swagger_auto_schema(
    method="post",
    request_body=openapi.Schema(
        title='xxx',
        type=openapi.TYPE_STRING,
        description="使用登录用户申请token",
        example="""
                {
                "username":"admin",
                "password":"admin"
                }
            """
    ))
@api_view(['POST'])
def login(request):
    indata = request.data
    try:
        if not all([i in indata for i in ('username', 'password')]):
            return JsonResponse({"error": "参数错误"}, status=400)

        # 根据用户查询用户对象
        app = App.objects.get(username=indata['username'])
        # 验证密码是否正确
        if app.check_password(indata['password']):
            token, exp = app.create_token()
            return JsonResponse({'tokenType': 'bearer', 'expiresIn': exp, 'accessToken': token.decode()}, status=200)
        else:
            return JsonResponse({"error": "用户或密码错误"}, status=400)
    except Exception:
        return JsonResponse({"error": "用户或密码错误！"}, status=500)
