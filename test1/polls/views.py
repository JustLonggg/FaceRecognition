from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from polls.models import UserLogin, BookInfo, PersonInfo
from django.db.models import F, Q, Sum, Count, Max, Min, Avg 

def index(request):
    return render(request, 'polls/index.html')

def data(request):
    ## get 查询一条指定记录
    ## all 查询所有记录

    ## filter 查询满足条件的数据 得到查询集
    # 属性__exact = '...'(或用简写 属性='...')   模糊查找 属性__contains = '...' 相当于数据库 like %...%
    # 以 ... 结尾：属性__endswith = '...'    以 ... 开头：属性__startswith = '...'
    # 以上都区分大小写 方法前加上i表示不区分 如 iexact ， icontains、
    # 常见的方法：
    # isnull； in； gt 大于； gte 大于等于； lt 小于； lte 小于等于； year; month; dat; weekdat;...

    ## exclude 查询不满足条件的数据 查询集

    ## 和另一个属性进行比较： F对象
    # user = UserLogin.objects.get(id=1)
    # ret = str(user.id) + ', ' + user.mail_address + ', ' + str(user.password)

    ## 进行 逻辑或 运算: Q对象 filter(Q() | Q()) ； 逻辑与运算：filter(..., ...) 
    # Q对象前加上 ‘~’ 表示 not

    ## 聚合函数 aggregate 包含 Sum, Avg, Max, Min, Count
    # 返回值为字典形式 如{'password_sum': 324545} 注意都是小写

    users = UserLogin.objects.all()    # 可以进行切片，但不支持负值
    # all函数以 ‘查询集’的形式返回所有数据表中的记录，不会立即执行
    # 只有使用了查询集中的数据时才会执行查询

    # 默认查询会使用objects，定义了管理器类后，要使用管理器类对象来查询
    # book = BookInfo.bookm.all()   
    print(type(users[0]))
    ret = ''
    for user in users:
        ret += str(user.id) + ', ' + user.mail_address + ', ' + str(user.password)
        ret += '<br>'
    return HttpResponse(ret)

## 多表查询： 一对多
def search(request):
    ## 使用对象查询
    # 第一种方法: 一到多查询： 查询三国演义中的所有人物
    book = BookInfo.objects.get(title='三国演义')
    persons = book.personinfo_set.all()   # 注意小写

    # 第二种方法： 多到一查询： 查询孙悟空对应的图书名称
    person = PersonInfo.objects.get(name='孙悟空')
    book = person.hbook   # 外键的属性名
    ret = book.title 


    ## 使用模型类查询
    # 多到一查询： 查询图书，要求图书中人物名字包含'空'
    # 一类模型类名.objects.filter(小写多类模型类名__属性名__条件运算符 = 值)
    books = BookInfo.objeacts.filter(personinfo__name__contains='空')

    # 一到多查询： 查询'西游记'中的所有人物
    # 多类模型类类名.objects.filter(多类模型类外键对应的属性名__一类模型类属性名__条件运算符 = 值)
    persons = PersonInfo.objects.filter(hbook__btitle__exact='西游记')

    ## 也可以使用原生的sql语句来查询：类.objects.raw('''select .... ''')
    # 得到的是rawqueryset类型，相当于列表

    return HttpResponse(ret)

def login(request):
    return render(request, 'polls/login.html')

def loginview(request):
    username = request.POST.get('username')   # 获得文本框的内容
    password = request.POST.get('passwd')
    gender = request.POST.get('gender')   # 获得段选框的内容
    hobbys = request.POST.getlist('hobby')    # 获得多选框checkbox的内容，以列表的形式，此时hobbys是一个list
    address = request.POST.get('address')     # 获得下拉列表的内容
    if username == 'zhang3' and password == '123':
        return render(request, 'polls/welcome.html')
    else:
        return render(request, 'polls/login.html')