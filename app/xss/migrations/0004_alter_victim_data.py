# Generated by Django 3.2.3 on 2021-05-29 15:26

import app.xss.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xss', '0003_victim_is_view'),
    ]

    operations = [
        migrations.AlterField(
            model_name='victim',
            name='data',
            field=models.JSONField(default=app.xss.models.return_object, verbose_name='数据'),
        ),
    ]