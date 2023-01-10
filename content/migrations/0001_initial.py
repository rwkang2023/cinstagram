# Generated by Django 3.2.16 on 2023-01-10 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(help_text='언제는 빼도, [어디]인지는 적어 주세요!')),
                ('image', models.TextField()),
                ('profile_image', models.TextField()),
                ('user_id', models.TextField()),
                ('use_email', models.CharField(blank=True, help_text='Email 좀 적어 주세요!', max_length=100)),
            ],
        ),
    ]
