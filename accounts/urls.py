from django.urls import path, include, re_path
from . import views
from .views import login_view,logout_view,signup_view, profile_view
urlpatterns = [
	path('signup/',signup_view,name='signup'),
	path('login',login_view , name='login'),
	path('logout',logout_view , name='logout'),
	re_path(r'^(?P<id>\w+)/$',profile_view,name='profile'),
	

]