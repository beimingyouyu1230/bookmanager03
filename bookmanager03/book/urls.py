from django.urls import path
from book.views import index,book,login,weibo

urlpatterns = [
    path('index/',index),
    # path('1/100/',book)
    path('<cat_id>/<detail_id>/',book),
    # <>占位符
    # 相当于 <cat_id> = 1
    # 相当于 <detail_id> = 100
    path('login/', login),
    path('weibo/', weibo)

]