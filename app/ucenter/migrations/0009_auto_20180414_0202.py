# Generated by Django 2.0.4 on 2018-04-13 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ucenter', '0008_user_is_vip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
    ]