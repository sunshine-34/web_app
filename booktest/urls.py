from django.urls import re_path
from booktest.views import TestView, HeroView


urlpatterns = [
    re_path(r'^heros/$', TestView.as_view()),
    # re_path(r'^login/$', views.login),
    # 类视图URL地址配置
    # re_path(r'^login/$', views.LoginView.as_view()),
    re_path(f'^heros/(?P<id>\d+)/$', HeroView.as_view())
]
