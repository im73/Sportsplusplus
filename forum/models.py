from django.db import models

# Create your models here.


class User(models.Model):

    username = models.CharField(max_length=20, primary_key=True,null=False, verbose_name=u"用户名")
    userlogo = models.ImageField(upload_to='', verbose_name=u"用户头像", null=True)

    class Meta:

        verbose_name = u"作者"
        verbose_name_plural = verbose_name


class Post(models.Model):
    postId = models.CharField(max_length=50, primary_key=True, null=False, verbose_name=u"帖子标题")
    content = models.CharField(max_length=254, primary_key=True, null=False,verbose_name=u"帖子内容")
    sendtime = models.DateTimeField(auto_now_add=True, verbose_name=u"发帖时间")

    username = models.ForeignKey(to="User", to_field="username", on_delete=models.CASCADE, verbose_name=u"帖子作者")
    userlogo = models.ForeignKey(to="User", to_field="userlogo", on_delete=models.CASCADE, verbose_name=u"帖子作者头像")

    class Meta:

        verbose_name = u"帖子"
        verbose_name_plural = verbose_name


class SubPost(models.Model):
    subPostId = models.CharField(max_length=50, primary_key=True, null=False, verbose_name=u"副帖子标题") # 副帖子标题？还是什么？
    subContent = models.CharField(max_length=254, primary_key=True, null=False,verbose_name=u"副帖子内容")
    subSendtime = models.DateTimeField(auto_now_add=True, verbose_name=u"副帖子发帖时间")

    postId = models.ForeignKey(to="Post", to_field="postId", on_delete=models.CASCADE, verbose_name=u"所属帖子")
    username = models.ForeignKey(to="User", to_field="username", on_delete=models.CASCADE, verbose_name=u"副贴作者")
    userlogo = models.ForeignKey(to="User", to_field="userlogo", on_delete=models.CASCADE, verbose_name=u"副贴作者头像")


    class Meta:

        verbose_name = u"副帖子"
        verbose_name_plural = verbose_name


class Reply(models.Model):
    rplContent = models.CharField(max_length=254, primary_key=True, null=False, verbose_name=u"回复内容")
    rpltime = models.DateTimeField(auto_now_add=True, verbose_name=u"回复时间")

    subPostId = models.ForeignKey(to="Post", to_field="postId", on_delete=models.CASCADE, verbose_name=u"所属副帖子")
    username = models.ForeignKey(to="User", to_field="username", on_delete=models.CASCADE, verbose_name=u"回复作者")
    userlogo = models.ForeignKey(to="User", to_field="userlogo", on_delete=models.CASCADE, verbose_name=u"回复作者头像")

    class Meta:

        verbose_name = u"回复"
        verbose_name_plural = verbose_name