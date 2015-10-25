from django.conf.urls import url
from . import views 

urlpatterns = [
	url(r'^$',views.index,name='index'),
	url(r'^register/$',views.register,name='register'),
	url(r'^institute/$',views.institute,name='institute'),
	url(r'^register_user/$',views.register_user,name="register_user"),
	url(r'^login/$',views.login,name="login"),
	url(r'^logout_user/$',views.logout_user,name="logout_user"),
	url(r'^update/(?P<id>[0-9]+)/$',views.update,name="update"),
	url(r'^update_user/(?P<id>[0-9]+)/$',views.update_user,name="update_user"),
	url(r'^home_page/(?P<id>[0-9]+)/$',views.home_page,name="home_page"),
	url(r'^update_profile/(?P<id>[0-9]+)/$',views.update_profile,name="update_profile"),
	url(r'^message/(?P<ids>[0-9]+)/$',views.message,name="message"),
	url(r'^messages/(?P<id>[0-9]+)/$',views.messages,name="messages"),
]	
