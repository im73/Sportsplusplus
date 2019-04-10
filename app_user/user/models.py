from django.db import models

# Create your models here.


class User(models.Model):

    register_time=models.DateTimeField(auto_now_add=True,verbose_name=u"注册时间")
    email=models.EmailField(verbose_name=u"邮箱",unique=True)
    nick_name=models.CharField("昵称",max_length=12,null=False,default='',unique=True)
    password=models.CharField(max_length=16,verbose_name=u"密码")
    image=models.ImageField(upload_to="image/%Y/%M",default="image/default.jpg",verbose_name=u"头像")

    class Meta:
        verbose_name = u"用户"
        verbose_name_plural = verbose_name


class back_user(models.Model):

    username=models.CharField(max_length=15,null=False,default="",unique=True)
    password=models.CharField(max_length=15,null=False,default="")

    class Meta:
        verbose_name = u"管理人员"
        verbose_name_plural = verbose_name

class email_very(models.Model):

    email = models.EmailField(verbose_name=u"邮箱",unique=True)
    very_code = models.CharField(max_length=10,verbose_name=u"验证码")
    op_type = models.IntegerField(verbose_name=u"操作类型")
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = u"验证码"
        verbose_name_plural = verbose_name
        ordering = ('date',)

