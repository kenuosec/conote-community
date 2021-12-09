# Generated by Django 2.0.4 on 2018-06-28 02:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Envelope',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(blank=True, max_length=512, null=True, verbose_name='标题')),
                ('mail_from', models.EmailField(blank=True, max_length=254, null=True, verbose_name='发件人')),
                ('path', models.FilePathField(verbose_name='原始文件位置')),
                ('send_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='原始发送时间')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('last_modify_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
            options={
                'verbose_name': '邮件',
                'verbose_name_plural': '邮件',
                'ordering': ['-created_time'],
            },
        ),
        migrations.CreateModel(
            name='MailBox',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='邮件地址')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('last_modify_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mail_boxes', to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '邮箱',
                'verbose_name_plural': '邮箱',
                'ordering': ['-created_time'],
            },
        ),
        migrations.AddField(
            model_name='envelope',
            name='mailbox',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='disposable_email.MailBox', verbose_name='邮箱'),
        ),
    ]