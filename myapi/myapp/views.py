from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.views import APIView

from myapp.models import MyappModel
from myapp.serializers import StudentInfoSerializer


class MyView(viewsets.ModelViewSet):
    serializer_class = StudentInfoSerializer
    queryset = MyappModel.objects.all()

