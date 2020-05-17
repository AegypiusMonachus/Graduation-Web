from django.shortcuts import render
from django.http import HttpResponse
from system.settings import BASE_DIR
from django.core.urlresolvers import reverse
import time,os,re
# 用于判断两个列表是否相等
import operator
from . import models

# 数据分页
from django.core.paginator import Paginator
# Create your views here.

# 登录界面
def studentlogin(request):

    if request.method == 'GET':
        # 返回登录界面
        return render(request,'student/login.html')

    elif request.method == 'POST':
        try:
            # 查询所有学生信息
            studet_data = models.students.objects.values('student_id','password')
            xh = [] # 学生学号
            pwd = [] # 密码
            for i in studet_data:
                xh.append(i['student_id'])
                pwd.append(i['password'])
            if request.POST['username'] in xh and request.POST['password'] == pwd[xh.index(request.POST['username'])]:
                # 把登录信息写入session中
                # request.session['AdminUser'] = {'username':'admin'}
                student_name = models.students.objects.filter(student_id = request.POST['username']).values('name')
                request.session['AdminUser'] = {'username':student_name[0]['name'],'student_ID':request.POST['username'],'password':request.POST['password']}
                # 执行登录
                return HttpResponse('<script>alert("登录成功");location.href="/student/books/index/";</script>')
            return HttpResponse('<script>alert("登录失败");location.href="/student/login/";</script>')
        except:
            return HttpResponse('<script>alert("登录失败");location.href="/student/login/";</script>')

# 后台退出
def studentlogout(request):
    request.session['AdminUser'] = ''
    request.session['student_ID'] = ''
    request.session['password'] = ''
    return HttpResponse('<script>alert("退出登录！");location.href="'+reverse('student_login')+'"</script>')

# 消息列表
def message(request):
    # 获取所有消息
    data = models.Message.objects.all()
    context = {'info_data':data}
    # return render(request,'student/message.html')
    return render(request,'student/message.html',context) 

def msgDetail(request):
    Id = request.GET.get('isbn')
    msg = models.Message.objects.get(id=Id)
    data = {
        "title":msg.title,
        "content":msg.content,
        "time":msg.time.strftime("%Y-%m-%d %H:%M:%S")
    }
    return render(request, "student/message-detail.html",data)

# 教材显示视图
def booksindex(request):   
    # 获取所有教材信息
    data = models.books.objects.all()
    # 获取搜索条件
    types = request.GET.get('types')
    keywords = request.GET.get('keywords')
    # 判断是否有搜索条件
    if types:
        # 判断搜索的类型
        if types == 'all':
            data = data
        else:
            search = {types+'__contains':keywords}
            data = data.filter(**search)   
    # 实例化分页类
    paginator = Paginator(data,10)
    # 获取当前页码数
    p = request.GET.get('p',1)
    # 获取当前页的数据
    book_data = paginator.page(p)
    # 数据分配
    context = {'books_data':book_data}
    return render(request,'student/books-list.html',context)

# 教材“购物车”列表
def booksorder(request):
    # 获取登录学生的学号
    stu_id = request.session['AdminUser']['student_ID']
    try:
        # 获取当前学生添加到购物车的教材
        books_data = models.Bookscart.objects.filter(stu_id=stu_id)
        books_isbn = []
        for book in books_data:
            books_isbn.append(book.isbn_id)
        books = models.books.objects.filter(book_isbn__in=books_isbn)
        total_price = 0.0
        for book_price in books:
            total_price += book_price.price
        context = {'books_data':books,'total_price':total_price}
        return render(request,'student/books-plan-list.html',context)

    except:
        return render(request,'student/books-list.html',context)    

# 教材添加至购物车
def booksadd(request):
    try:
        # 获取学生id（学号）、教材ISBN
        stu_id = request.session['AdminUser']['student_ID']
        isbn = request.GET.get('isbn')

        # 检查当前的教材是否已经存在教材预定列表中
        result = models.Bookscart.objects.filter(isbn_id=isbn).filter(stu_id=stu_id)
        if result:
            return HttpResponse('<script>alert("该教材已经加入预定列表！");location.href="'+reverse('student_books_index')+'"</script>')
        else:
            # 添加至数据库
            db = models.Bookscart(stu_id=stu_id,isbn_id=isbn)
            db.save()

        return HttpResponse('<script>alert("加入预定列表成功！");location.href="'+reverse('student_books_index')+'"</script>')
    except:
        return render(request,'student/books-list.html')
    
#删除教材列表中的某教材
def booksdel(request,isbn):
    try:
        # 获取学生学号
        stu_id = request.session['AdminUser']['student_ID']
        bdata = models.Bookscart.objects.filter(stu_id=stu_id).filter(isbn_id=isbn)
        bdata.delete()

        return HttpResponse('<script>alert("删除该教材成功！");location.href="'+reverse('student_books_order')+'"</script>')
    except:
        return HttpResponse('<script>alert("删除该教材失败！");location.href="'+reverse('student_books_order')+'"</script>')

# 确认订购教材
def booksconfirm(request):
    # 获取登录学生的学号
    stu_id = request.session['AdminUser']['student_ID']
    search_dict = dict()
    search_dict['stu_id'] = stu_id
    search_dict['status'] = 0
    # 查询该学生教材订购表中的现存数据
    isbns = models.BooksOrder.objects.filter(**search_dict).values('isbn')
    stu_isbns = []
    for isbn in isbns:
        stu_isbns.append(isbn['isbn'])
    print(stu_isbns)
    # 接受预定教材的isbn
    books_isbn = request.GET.get('books_isbn')
    # 正则表达式
    zz = "\"([^\"]*)\""
    res = re.findall(zz,books_isbn)
    print(res)
    if not res:
        return HttpResponse('<script>alert("没有选中教材，订购失败！");location.href="'+reverse('student_books_index')+'"</script>')
    if operator.eq(stu_isbns, res):
        return HttpResponse('<script>alert("本次提交的教材情况跟上次一样，订购失败！");location.href="'+reverse('student_books_order')+'"</script>')
    if not operator.eq(stu_isbns, res):
        # 查询该学生教材订购表中的现存数据
        stu_books = models.BooksOrder.objects.filter(**search_dict)
        stu_books.delete()
        for book_isbn in res:
            # 添加至教材订购表中
            db1 = models.BooksOrder(stu_id=stu_id,isbn=book_isbn)
            db1.save()
            # 删除至购物车表中的数据
            db2 = models.Bookscart.objects.filter(stu_id=stu_id).filter(isbn_id=book_isbn)
            db2.delete()

        return HttpResponse('<script>alert("订购教材成功！");location.href="'+reverse('student_books_buy')+'"</script>')

# 个人教材订购情况
def booksbuy(request):
    # 获取学生id（学号）
    stu_id = request.session['AdminUser']['student_ID']
    books_data = models.BooksOrder.objects.filter(stu_id=stu_id).values('isbn')
    books_isbn = []
    for book in books_data:
        books_isbn.append(book['isbn'])
    books = models.books.objects.filter(book_isbn__in=books_isbn)
    total_price = 0.0
    for book_price in books:
        total_price += book_price.price
    context = {'books_data':books,'total_price':total_price}   
    return render(request,'student/books-buy-list.html',context)

# 个人信息
def studentinfo(request):
    id = request.session['AdminUser']['student_ID']
    student_info = models.students.objects.get(student_id = id)
    return render(request,'student/person-info.html',{'student_info':student_info})

# 修改个人密码
def studentpwd(request):
    # 判断当前的请求方式
    if request.method == 'GET':
        # 加载表单页面
        return render(request,'student/edit-password.html')

    elif request.method == 'POST':
        # 获取登录学生的学号
        stu_id = request.session['AdminUser']['student_ID']
        password = request.session['AdminUser']['password']
        # 接收数据,进行数据
        data = request.POST.dict()
        data.pop('csrfmiddlewaretoken')
        if password != data['oldPwd']:
            return HttpResponse('<script>alert("原密码输入错误，修改失败！");location.href="'+reverse('student_pwd')+'"</script>')
        if len(data['newPwd']) < 6 or len(data['newPwd']) >15:
            return HttpResponse('<script>alert("新密码格式不正确，修改失败！");location.href="'+reverse('student_pwd')+'"</script>')
        if data['newPwd'] != data['twicePwd']:
            return HttpResponse('<script>alert("输入的两次新密码不一致，修改失败！");location.href="'+reverse('student_pwd')+'"</script>')
        pwd = models.students.objects.get(student_id = stu_id)
        pwd.password = data['newPwd']
        pwd.save()

        return HttpResponse('<script>alert("密码修改成功！");location.href="'+reverse('student_logout')+'"</script>')
    
    


# 班级教材订购
def classOrder(request):
    
    return render(request,'student/class-books-buy.html')
    # return render(request,'student/message.html',context) 

# 班级教材图形化
def classOrderPicture(request):
    
    return render(request,'student/class-books-buy-web.html')
    # return render(request,'student/message.html',context) 