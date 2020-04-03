from django.conf.urls import url
from django.urls import path

from myapi.decorator import login_require
from myapp.views import MyView


urlpatterns = [
    path('api/test/v1', login_require(MyView.as_view({'get': 'list', 'post': 'create'}))),
]