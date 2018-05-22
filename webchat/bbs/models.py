from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import  ValidationError
#Django admin后台出错时抛出的红色错误提示，要自定义错误时需要引入此方法
import datetime

# Create your models here.

# 论坛帖子表
class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name=u"标题") # 字符串字段
    brief = models.CharField(null=True, blank=True, max_length=255, verbose_name=u"描述")

    # 由于Category类在它的下方,所以要引号引起来,Django内部会自动反射去找
    category = models.ForeignKey("Category", verbose_name=u"所属板块",on_delete=models.CASCADE,)  # ForeignKey定义多对一
    content = models.TextField(verbose_name=u"文章内容") # 字符串=longtext
    head_img = models.ImageField(verbose_name=u"文章标题图片", upload_to="uploads")
    # 默认你如果不设置upload_to,会在Django项目目录根目录下保存上传文件,此字段只存储 文件路径/文件名
    # 当我们结合前端上传文件时,也不会用upload_to 设置上传文件的保存路径,为啥不用,后面会说
    author = models.ForeignKey("UserProfile", verbose_name=u"作者",on_delete=models.CASCADE,)
    pub_date = models.DateField(blank=True, null=True, verbose_name=u"创建时间") # 日期
    last_modify = models.DateField(auto_now=True, verbose_name=u"修改时间")
    # 需要注意的是一旦设置auto_now=True ,默认在admin后台就是非编辑状态了,也就是在admin后台此字段为隐藏,除非手动设置可编辑属性
    # auto_now 用于修改,auto_now_add用于创建,在admin后台都是默认不可编辑(隐藏)

    priority = models.IntegerField(default=1000, verbose_name=u"优先级")
    status_choices = (('draft', u"草稿"),
                      ('published', u"已发布"),
                      ('hidden', u"隐藏"),
                      )
    status = models.CharField(max_length=64, choices=status_choices, default="published")

    def __str__(self):
        return self.title

    # django 的model类在保存数据时,会默认调用self.clean()方法的,所以可以在clean方法中定义数据的一些验证
    def clean(self):
        # 如果帖子有发布时间,就说明是发布过的帖子,发布过的帖子就不可以把状态在改成草稿状态了
        if self.status == "draft" and self.pub_date is not None:
            raise ValidationError(u"如果你选择草稿,就不能选择发布日期!")
        # 如果帖子没有发布时间,并且保存状态是发布状态,那么就把发布日期设置成当天
        if self.status == 'published' and self.pub_date is None:
            self.pub_date = datetime.date.today()

    class Meta:
        verbose_name = u"帖子表"

# 评论表
class Comment(models.Model):
        pass

# 板块表
class Category(models.Model):
    pass

# 用户表继承Django里的User
class UserProfile(models.Model):
    pass

# 用户组表
class UserGroup(models.Model):
    pass