# Generated by Django 2.1.1 on 2018-09-17 16:48

from django.db import migrations, models


def nop(*args, **kwargs):
    pass


def set_category(apps, schema_editor):
    Note = apps.get_model('log', 'Note')
    for note in Note.objects.all():
        if note.is_markdown:
            note.category = 'article'
        elif note.attachment:
            note.category = 'file'
        elif note.language:
            note.category = 'code'
        else:
            note.category = 'text'

        note.save()


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0020_auto_20180403_2031'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='category',
            field=models.CharField(choices=[('text', '纯文本'), ('file', '文件'), ('article', '文章'), ('code', '代码')], default='text', max_length=16, verbose_name='类型'),
        ),
        migrations.RunPython(set_category, nop),
    ]