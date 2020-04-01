"""为应用程序users定义url模式"""

from django.urls import path
from django.contrib.auth.views import LoginView

from . import views

app_name = 'users'

urlpatterns = [
    # 登陆页面
    path('login/',LoginView.as_view(template_name='users/login.html'),
        name='login'),
    # 注销
    path('logout/',views.logout_view,name='logout'),
    # 注册新用户
    path('register/',views.register,name='register'),
]