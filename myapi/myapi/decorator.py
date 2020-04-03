from functools import wraps

import jwt
from django.http import JsonResponse

from myapi.settings import SECRET_KEY
from authTest.models import App


def login_require(view):
    @wraps(view)
    def decorator(request, *args, **kwargs):
        auth_jwt = request.META.get('HTTP_ACCESSTOKEN')
        if auth_jwt:
            try:
                auth_res = jwt.decode(auth_jwt, SECRET_KEY)
            except:
                return JsonResponse({'authError': 'Authorize Failed'}, status=401)
            app = App.objects.filter(username=auth_res.get('headers').get('user_id')).first()
            request.appUser = app
            request.appAuth = auth_jwt
            return view(request, *args, **kwargs)
        else:
            return JsonResponse({'authError': 'accessToken  not found in request headers'},status=401)
    return decorator
