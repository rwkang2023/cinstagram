# Generated by Django 3.2.16 on 2023-01-10 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feed',
            name='use_email',
        ),
        migrations.AddField(
            model_name='feed',
            name='user_email',
            field=models.CharField(choices=[('RW', 'rwkang@naver.com'), ('HK', 'hkyun@naver.com')], default='RW', help_text='Email 좀 적어 주세요!', max_length=2),
        ),
    ]
