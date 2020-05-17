from django import template
register = template.Library()

from django.utils.html import format_html

# 自定义 分页 标签
@register.simple_tag
def showpages(count,request):
    # count 总页数
    # p 当前页码数
    # 每回显示10个页码数

    p = int(request.GET.get('p',1))

    # 总页码数不到10页
    if count < 10:
        begin = 1
        end = count
    # 当前页码数加5小于等于10页
    elif p + 5 <= count:
        # 当前页码数小于等于5
        if p <= 5:
            begin = 1
            end = 10
        # 当前页码数大于5
        if p > 5:
            begin = p - 4
            end = p + 5
    # 当前页码数加5大于10页
    elif p + 5 > count:
        begin = count - 9
        end = count

    # 获取页面上的其它搜索条件 &types=username&keywords=da
    data = request.GET.dict()
    # 删除获取的页码数
    data.pop('p',None)
    # 获取搜索条件 condition条件
    condition = ''
    for k,v in data.items():
        condition += '&'+k+'='+v

    # 分页
    pages = ''
    # 首页
    if p > 1:
        pages += '<li><a href="?p=1">首页</a></li>'
    # 上一页
    if p > 1:
        pages += '<li><a href="?p='+str(p-1)+condition+'">«</a></li>'

    for i in range(begin,end+1):
        # 判断是否在当前页
        if i == p :
            pages += '<li class="am-active"><a href="?p='+str(i)+condition+'">'+str(i)+'</a></li>'
        else:
            pages += '<li><a href="?p='+str(i)+condition+'">'+str(i)+'</a></li>'

    # 下一页
    if p < count:
        pages += '<li><a href="?p='+str(p+1)+condition+'">»</a></li>'

    # 尾页
    if p < count:
        pages += '<li><a href="?p='+str(count)+'">尾页</a></li>'

    return format_html(pages)