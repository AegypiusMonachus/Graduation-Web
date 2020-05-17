"""system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    # 登录界面
    url(r'^login/$',views.studentlogin,name='student_login'),
    # 退出登录
    url(r'^logout/$',views.studentlogout,name='student_logout'),

    # 消息列表
    url(r'^message/$',views.message,name='student_message'),
    url(r'^message/detail/$',views.msgDetail,name='student_message_detail'),

    # 教材展示
    url(r'^books/index/$',views.booksindex,name='student_books_index'),
    
    # 教材添加至教材预定列表
    url(r'^books/add/$',views.booksadd,name='student_books_add'),
    # 教材预定列表页
    url(r'^books/order/$',views.booksorder,name='student_books_order'),
    url(r'^books/del/(?P<isbn>[0-9]+)/$',views.booksdel,name='student_books_del'),
    # 预定的教材存入订单表
    url(r'^books/confirm/$',views.booksconfirm,name='student_books_confirm'),

    # 教材订购情况
    url(r'^books/buy/$',views.booksbuy,name='student_books_buy'),

    # 个人信息
    url(r'^student/info/$',views.studentinfo,name='student_info'),
    # 修改密码
    url(r'^student/pwd/$',views.studentpwd,name='student_pwd'),

    # 班级
    url(r'^class/order/books/$',views.classOrder,name='class_order_books'),
    url(r'^class/order/picture$',views.classOrderPicture,name='class_order_picture'),
]