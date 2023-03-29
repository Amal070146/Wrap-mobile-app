from .views import signup,admin_home,get_start,select_occupation,loader,login_admin,signin,user_logout,admin_logout
from .views import track,booking,rewards,dashboard,redeem
from .views import report,pickup,purchase,dropoff
from .views import profile,notification,edit_profile,delete_user,support_profile,contact_us
from django import contrib
from django.urls import include,path

urlpatterns = [
    path('',loader, name='loader'),
    path('get_start/',get_start,name='get_start'),
    path('select_occupation/',select_occupation,name='select_occupation'),
    path('signup/',signup, name='signup'),
    path('signin/',signin, name='signin'),
    path('login_admin/',login_admin, name='login_admin'),
    path('admin_home/',admin_home, name='admin_home'),
    path('admin_logout/',admin_logout, name='admin_logout'),
    path('user_logout/',user_logout, name='user_logout'),

    path('dashboard/',dashboard, name='dashboard'),
    path("booking/",booking,name='booking'),
    path('rewards/',rewards,name='rewards'),
    path('track/',track,name='track'),
    path('redeem/',redeem,name='redeem'),
    
    path('dropoff/',dropoff,name='dropoff'),
    path('pickup/',pickup,name='pickup'),
    path('purchase/',purchase,name='purchase'),
    path('report/',report,name='report'),

    path('profile/',profile,name='profile'),
    path('notification/',notification,name='notification'),
    path('edit_profile/',edit_profile,name='edit_profile'),
    path('support_profile/',support_profile,name='support_profile'),
    path('delete_user/',delete_user,name='delete_user'),
    path('contact_us/',contact_us,name='contact_us'),
]