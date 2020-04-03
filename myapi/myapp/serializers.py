# 定义一些序列化程序
from rest_framework import serializers

from myapp.models import MyappModel


class StudentInfoSerializer(serializers.ModelSerializer):
    '''创建序列化器'''
    class Meta:
        model = MyappModel  # 数据库表名
        fields = '__all__' # 所有的字段都要
        # fields = ('no', 'name', 'sex')
        # 注册Book下面那些字段

