from django.db import models

# Create your models here.


class MyappModel(models.Model):
    class Meta:
        db_table = 'student'

    no = models.IntegerField( primary_key=True)
    name = models.CharField(max_length=200)
    sex = models.TextField(max_length=100)
    math = models.IntegerField(blank=True, null=True)
    chinese = models.IntegerField(blank=True, null=True)




