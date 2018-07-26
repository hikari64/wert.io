from django.urls import path, include, re_path
from . import views
from django.views.generic.base import TemplateView
from .views import login_view,logout_view,home_view,signup_view, profile_view
urlpatterns = [
	path('',home_view,name='home'),
	path('signup/',signup_view,name='signup'),
	path('login',login_view , name='login'),
	path('logout',logout_view , name='logout'),
	re_path(r'^(?P<id>\w+)/$',profile_view,name='profile'),
	

]