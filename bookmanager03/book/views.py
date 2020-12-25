from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):

    return HttpResponse('登录页面')


def book(request,cat_id,detail_id):

    # print(cat_id,detail_id)

    # 获取字符串所有数据 http://127.0.0.1/1/100/?a=10&b=20
    query_string=request.GET
    # print(query_string)
    # < QueryDict: {'a': ['10'], 'b': ['20']} >
    # a=query_string['a']
    # b=query_string.get('b')
    # print(a,b)

    # 字典：key:value一键一值(一般)
###################查询获取字符串#######################
    # 输入网址http://127.0.0.1/1/100/?a=10&b=20&a=666
    # print(query_string)
    # <QueryDict: {'a': ['10', '666'], 'b': ['20']}>
    '''
    结论：
    QueryDict
    可以一键一值，也可以一建多值
    一键一值  ===>>>  QueryDict_data.get(key)
    一建多值  ===>>>  QueryDict_data.getlist(key)
    '''
    # 正常使用：
    alist=query_string.getlist('a')
    b=query_string.get('b')
    print(alist,b)


    # get(key.key值不存在使用默认值)
    page=query_string.get('page',1)
    print(page)

    return HttpResponse('我喜欢看书')

def login(request):
    # < QueryDict: {'username': ['itcast'], 'password': ['123']} >
    body=request.POST
    print(body)
    return HttpResponse('login')

def weibo(request):
    # JSON数据的接受是在request.body中
    # 1.接收参数
    body=request.body
    print(body)
    # b'{\n\t"name":"itcast",\n\t"age":10\n}'

    # 2.将bytes类型的数据转换成字符串str类型(是json形式的字符串）
    body_str=body.decode()
    print(body_str)
    '''
    {
        "name":"itcast",
        "age":10
}

    '''

    # 3.将json形式的字符串类型转换成字典dict类型
    import json
    data=json.loads(body_str)
    print(data)
    # {'name': 'itcast', 'age': 10}

    return HttpResponse('weibo json')