from .views import signup,admin_home,get_start,loader,login_admin,signin,user_logout,admin_logout
from .views import track,booking,rewards,dashboard
from django import contrib
from django.urls import include,path

urlpatterns = [
    path('',loader, name='loader'),
    path('get_start/',get_start,name='get_start'),
    path('signup/',signup, name='signup'),
    path('signin/',signin, name='signin'),
    path('login_admin/',login_admin, name='login_admin'),
    path('admin_home/',admin_home, name='admin_home'),
    path('admin_logout/',admin_logout, name='admin_logout'),
    path('user_logout/',user_logout, name='user_logout'),
    path('dashboard/',dashboard, name='dashboard'),
    path("booking/",booking,name='booking'),
    path('rewards/',rewards,name='rewards'),
    path('track/',track,name='track')

]