from django.db import models

# Create your models here.

# MVT 数据模型
# ORM 数据模型
# 在此处编写应用的数据类型
# 每一张表就是一个模型类
# 有了ORM 之后我们就可以定义出表对应的模型类
# 通过操作模型类去操作数据库  不需要写sql语句

# 有了模型类之后模型类如何与数据库交互
# 1注册模型 在setting.py中的INSTALLED_APPS 添加应用名
# 2生成迁移文件 用于与数据库交互 python manage.py makemigrations 会在对应的应用下方生成迁移文件，不需要关注
# 3执行迁移 会在对应的数据库中生成的对应的表python manage.py migrate

class Book(models.Model):
    """
    hero 继承了Model类  应为Model类拥有操作数据库功能
    """
    title = models.CharField(max_length=20)
    price = models.FloatField(default=0)
    pub_date= models.DateField(default="1993-06-14")
    auther = models.CharField(max_length=20,default="lijb")
    desc = models.CharField(max_length=50,null=True,blank=True,db_column="description",help_text="请输入书籍备注信息")
    # teletephon = models.CharField(max_length=11,unique=True)
    def __str__(self):
        return self.title


class Hero(models.Model):
    """
    hero 继承了Model 也可以操作数据库
    """
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=6,choices=(('male','男'),('female','女')),default='male')
    content = models.CharField(max_length=100)
    # book 是一对多中的外键on_delete代表删除主表数据时如何做
    book = models.ForeignKey(Book,on_delete=models.CASCADE,related_name='heros')

    def __str__(self):
        return self.name
# django ORM关联查询
# 多方Hero  -方Book
# 1多找一  ，多方对象，关系字段 exp：h1.book
# 2一找多， 一方对象，小写多方类名 _set.all()  exp:  b1.hero_set.all():q

class UserManager(models.Manager):
    """
    自定义模型管理类  该模型不在具有objects对象
    """
    def deleteByTelePhone(self,tele):
        # django默认的objects 是Manager类型    *.objects.get()
        user = self.get(telephone=tele)
        user.delete()
    def createUser(self,tele):
        # self.model可以获取模型类构造函数
        user = self.model()
        # user = User()
        user.telephone = tele
        user.save()

class User(models.Model):
    telephone = models.CharField(max_length=11,null=True,blank=True,verbose_name="手机号码")
    # 自定义过管理字段之后不在有objects  自定义了一个新的objects
    objects = UserManager()
    def __str__(self):
        return self.telephone
    class Meta:
        # 表明
        db_table = "用户类"
        ordering = ["-telephone"]
        # admin页面进入模型类显示名字
        verbose_name = "用户模型类a"
        # admin 页面在应用下方显示的模型名
        verbose_name_plural = "用户模型类s"

class Account(models.Model):
    username = models.CharField(max_length=20,verbose_name="用户名")
    password = models.CharField(max_length=20,verbose_name="密码")
    regist_date = models.DateField(auto_now_add=True,verbose_name="注册日期")

class Concact(models.Model):
    telephon = models.CharField(max_length=11,verbose_name="手机号")
    email = models.EmailField(default="158883967@qq.com")
    account = models.OneToOneField(Account,on_delete=models.CASCADE)



