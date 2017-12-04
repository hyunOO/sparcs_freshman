from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.login_login, name = 'login_login'),
	url(r'^login/$', views.login_login, name = 'login_login'),
	url(r'^signup/$', views.signup, name = 'signup'),
	url(r'^signup_signup/$', views.signup_signup, name = 'signup_signup'),
	url(r'^login_configure/$', views.login_configure, name = 'login_configure'),
    url(r'^folder/$', views.folder_list, name = 'folder_list'),
    url(r'^news/(?P<store_id>\d+)$', views.news_list, name = 'news_list'),
]