# Generated by Django 2.1.7 on 2019-04-11 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='back_user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=15, unique=True)),
                ('password', models.CharField(default='', max_length=15)),
            ],
            options={
                'verbose_name': '管理人员',
                'verbose_name_plural': '管理人员',
            },
        ),
        migrations.CreateModel(
            name='email_very',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='邮箱')),
                ('very_code', models.CharField(max_length=10, verbose_name='验证码')),
                ('op_type', models.IntegerField(verbose_name='操作类型')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '验证码',
                'verbose_name_plural': '验证码',
                'ordering': ('date',),
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('register_time', models.DateTimeField(auto_now_add=True, verbose_name='注册时间')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='邮箱')),
                ('nick_name', models.CharField(default='', max_length=12, unique=True, verbose_name='昵称')),
                ('password', models.CharField(max_length=16, verbose_name='密码')),
                ('image', models.ImageField(default='image/default.jpg', upload_to='image/%Y/%M', verbose_name='头像')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
            },
        ),
    ]
