from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
	url(r'^$',views.home),
	url(r'^login/$',login,{'template_name' : 'account/login.html'}),
	url(r'^logout/$',logout, {'template_name' : 'account/logout.html'}),
	url(r'^register/$',views.register, name = 'register'),
	#read data 
	url(r'^profile/$', views.profile, name = 'profile'),
	#edit
	url(r'^profile/edit/$', views.edit_profile, name = 'edit_profile'),
	
]
