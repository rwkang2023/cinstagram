# Generated by Django 3.2.16 on 2023-01-10 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_auto_20230110_2332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='user_email',
            field=models.CharField(blank=True, help_text='Email 좀 적어 주세요!', max_length=100),
        ),
    ]
