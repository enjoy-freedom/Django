# Generated by Django 2.1.10 on 2020-03-03 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authTest', '0003_app_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
        ),
    ]
