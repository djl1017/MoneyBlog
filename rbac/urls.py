from django.conf.urls import url

from . import views

urlpatterns = [
    # 菲律宾20K
    url(r'job/$', views.UserView.as_view()),
]