from django.db import models
from app_user.user.models import User
# Create your models here.





class Post(models.Model):

    postId = models.CharField(max_length=50, null=False, verbose_name=u"帖子标题")
    content = models.CharField(max_length=254, null=False,verbose_name=u"帖子内容")
    sendtime = models.DateTimeField(auto_now_add=True, verbose_name=u"发帖时间")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=u"帖子作者")


    class Meta:

        verbose_name = u"帖子"
        verbose_name_plural = verbose_name


class SubPost(models.Model):

    subPostId = models.CharField(max_length=100, null=False, verbose_name=u"副帖子标题") # 副帖子标题？还是什么？
    subContent = models.CharField(max_length=254,null=False,verbose_name=u"副帖子内容")
    subSendtime = models.DateTimeField(auto_now_add=True, verbose_name=u"副帖子发帖时间")

    postId = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name=u"所属帖子")
    user = models.ForeignKey(User,  on_delete=models.CASCADE, verbose_name=u"副贴作者")

    class Meta:

        verbose_name = u"副帖子"
        verbose_name_plural = verbose_name



class Reply(models.Model):

    rplContent = models.CharField(max_length=254,  null=False, verbose_name=u"回复内容")
    rpltime = models.DateTimeField(auto_now_add=True, verbose_name=u"回复时间")

    subPostId = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name=u"所属副帖子")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=u"回复作者")

    class Meta:

        verbose_name = u"回复"
        verbose_name_plural = verbose_name