# Generated by Django 3.1.3 on 2021-06-16 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0002_auto_20210616_1547'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='question',
            new_name='question_content',
        ),
        migrations.AlterField(
            model_name='question',
            name='grade',
            field=models.IntegerField(default=1),
        ),
    ]
