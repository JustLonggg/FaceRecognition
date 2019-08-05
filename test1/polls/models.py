from django.db import models

# Create your models here.

class UserLogin(models.Model):
    mail_address = models.CharField(max_length=50)
    password = models.IntegerField()
    identifying_code = models.CharField(max_length=10)

# 定义管理器类
class BookInfoManager(models.Manager):
    def all(self):  # 重写all方法
        # super是调用父类的方法，在父类查询的结果集上进行修改
        return super().all().filter(isDelete=False)

    def addBook(self, bookname, pubdate):
        book = self.model()    # 相当于 book = BookInfo()
        book.btitle = bookname
        book.bpub_date = pubdate
        book.save()

    def delBook(self):
        pass

    def selectBook(self):
        pass

## 一对多型数据表
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateField()

    bookm = BookInfoManager()    # 创建管理器类的对象，这是系统将不会再自动产生objects对象

class PersonInfo(models.Model):
    name = models.CharField(max_length=20)
    gender = models.BooleanField(default=True)
    # 关联外键
    hbook = models.ForeignKey('BookInfo',on_delete=models.CASCADE)


## 多对多型数据表
class TypeInfo(models.Model):
    tname = models.CharField(max_length=20)  # 新闻类别

class NewsInfo(models.Model):
    ntitle = models.CharField(max_length=60)
    ncontent = models.TextField()
    npub_date = models.DateTimeField(auto_now_add=True)

    # 通过ManyToManyField建立TypeInfo类和NewsInfo类之间的多对多的关系
    ntype = models.ManyToManyField('TypeInfo')


## 自连接型数据表
class AreaInfo(models.Model):
    atitle = models.CharField(max_length=30)

    # 自连接上级地区
    aParent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)