from django.db import models

# Create your models here.


class User(models.Model):

    register_time=models.DateTimeField(auto_now_add=True,verbose_name=u"注册时间")
    ph_number=models.CharField(max_length=11,null=False,default='',verbose_name=u"电话号码")
    nick_name=models.CharField(max_length=12,null=False,default='',verbose_name=u"昵称")
    image=models.ImageField(upload_to="image/%Y/%M",default="image/default.jpg",verbose_name=u"头像")


