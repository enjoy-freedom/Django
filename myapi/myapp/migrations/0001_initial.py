# Generated by Django 2.1.10 on 2020-03-04 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyappModel',
            fields=[
                ('no', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('sex', models.TextField(max_length=100)),
                ('math', models.IntegerField(blank=True, null=True)),
                ('chinese', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'student',
            },
        ),
    ]
