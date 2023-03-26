from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
import datetime
from .models import User, Admin,Booking,WrapUser
from .forms import ProfileForm
import folium

#loader and home\
def loader(request):
    return render(request,'loader.html')
def get_start(request):
    return render(request,'get_start.html')
# Admin pages

def admin_home(request):
    if 'aname' in request.session:
        data = {'name':request.session.get('aname')}
        return render(request,'admin_home.html',context=data)
    else:
        data = {'status':'You need to login first'}
        return render(request,'admin_login.html',context=data)
    
def login_admin(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')

        try:
            user = Admin.objects.get(name=name)

            if user.password == password:
                request.session['aname'] = name
                # return HttpResponse('ffaf')
                return admin_home(request)
            else:
                data = {'status':"Incorrect Password!!!"}
                return render(request,'admin_login.html',context=data)

        except Exception as e:
            data = {'status':"Invalid Username"}
            return render(request,'admin_login.html',context=data)
    else:
        return HttpResponse("Something went wrong faffsffa!!!!!")


def admin_logout(request):
    if 'aname' in request.session:
        del request.session['aname']

    return render(request,'admin_login.html')

#user registration
def signup(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        email = request.POST.get('email')
        photo = request.FILES.get('photo')
        password = request.POST.get('password')
        re_password = request.POST.get('repassword')

        if(password == re_password):
            user = User(name=name,email=email,photo=photo,password=password)
            user.save()
            email = [email]
            request.session['uname'] = name
            request.session['email'] = email
            return dashboard(request)
        else:
            data = {'status':"Password and Re-entered password must be same"}
            return render(request,'signup.html',context=data)
    else:
        return render(request, 'signup.html')
    
def signin(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.get(name=name,email=email)

        if user.password == password:
            request.session['uname'] = name
            request.session['email'] = email
            return redirect("dashboard")
        else:
            data = {'status':"Incorrect Password!!!"}
            return render(request,'signin.html',context=data)
    else:
        return render(request, 'signin.html')



def user_logout(request):
    if 'uname' in request.session:
        del request.session['uname']

    return render(request,'signin.html')

#User Home Page
def dashboard(request):
    if 'uname' in request.session:
        data = {'name':request.session.get('uname')}
        return render(request,'dashboard.html',context=data)
    else:
        data = {'status':'You need to login first'}
        return render(request,'sigin.html',context=data)
    
def booking(request):
    if 'uname' in request.session:
        data = {'name':request.session.get('uname')}
        bookings = Booking.objects.all()
        # return render(request,'booking.html',context=data)
        return render(request,'booking.html',{'bookings': bookings})
    else:
        data = {'status':'You need to login first'}
        return render(request,'signin.html',context=data)
    
def rewards(request):
    if 'uname' in request.session:
        data = {'name':request.session.get('uname')}
        return render(request,'rewards.html',context=data)
    else:
        data = {'status':'You need to login first'}
        return render(request,'signin.html',context=data)
    
def track(request):
    if 'uname' in request.session:
        data = {'name':request.session.get('uname')}
        m = folium.Map(location=[10.307897806699529,76.33507993927475], zoom_start=12)
        folium.Marker(location=[10.527627837215208, 76.21445706825584], popup="<p>Waste picked up</p>",
                  tooltip="11 AM", icon=folium.Icon(color="green")).add_to(m)
        folium.Marker(location=[10.512665164588398, 76.25561768977308], popup="<p>Reached collection point</p>",
                  tooltip="04:03 PM", icon=folium.Icon(color="green")).add_to(m)
        folium.Marker(location=[10.380721708232917, 76.2974580261964], popup="<p>Sent to Infinite waste LLC</p>",
                  tooltip="05:59 PM", icon=folium.Icon(color="green")).add_to(m)
        folium.Marker(location=[10.307003287734428, 76.33404101823123], popup="<p>On the way</p>",
                  tooltip="Just now", icon=folium.Icon(color="green")).add_to(m)
        trail_coordinates = [
            (10.527627837215208, 76.21445706825584),
            (10.523402028044528, 76.21676339524682),
            (10.519703423024081, 76.23536899988589),
            (10.516517757310858, 76.23639896810602),
            (10.512243214395411, 76.24628360262749),
            (10.512665164588398, 76.25561768977308),
            (10.511230531485214, 76.25838572952064),
            (10.44553925741713, 76.25895097511498),
            (10.438250590627376, 76.26464509672473),
            (10.434547789578632, 76.26604183367157),
            (10.413445049777307, 76.27076760239916),
            (10.394643441226956, 76.28688595976858),
            (10.387101170763309, 76.28899028286708),
            (10.383513125885708, 76.29289557903502),
            (10.380721708232917, 76.2974580261964),
            (10.371372889255452, 76.30409791447754),
            (10.370526874778777, 76.30986345834272),
            (10.371289720024908, 76.30407888007696),
            (10.370635399487753, 76.30944329789006),
            (10.367757892786981, 76.31390110718998),
            (10.357267374074375, 76.31662623143903),
            (10.351337316076425, 76.31821067557871),
            (10.34830617592037, 76.32067779967979),
            (10.341336158809888, 76.3223738294376),
            (10.337283183792525, 76.32153698025876),
            (10.32652276578376, 76.32295778284612),
            (10.31912449146524, 76.32680047441302),
            (10.311481803371343, 76.3310774898666),
            (10.307003287734428, 76.33404101823123)

        ]
        folium.PolyLine(trail_coordinates, tooltip="Coast",color="darkred").add_to(m)
        m = m._repr_html_()
        return render(request,'track.html',{ "m": m})
    else:
        data = {'status':'You need to login first'}
        return render(request,'signin.html',context=data)
    
#dashboard pages
def dropoff(request):
    if 'uname' in request.session:
        data = {'name':request.session.get('uname')}
        if request.method == 'POST':
            users  = User.objects.get(name=request.session['uname'])
            print(users.email)
            wastetype = request.POST.get('wastetype')
            date = request.POST.get('date')
            booking_address = request.POST.get('booking_address')
            print(date)
            book = Booking(wastetype=wastetype,name=users.name,uid=users.uid ,date=date,email=users.email, booking_address=booking_address)
            book.save()
            return render(request,'dashboard/success/pickup-success.html',context=data)
        return render(request,'dashboard/dropoff.html',context=data)
    else:
        data = {'status':'You need to login first'}
        return render(request,'signin.html',context=data)
    
def pickup(request):
    if 'uname' in request.session:
        data = {'name':request.session.get('uname')}
        if request.method == 'POST':
            users  = User.objects.get(name=request.session['uname'])
            print(users.email)
            wastetype = request.POST.get('wastetype')
            date = request.POST.get('date')
            booking_address = request.POST.get('booking_address')
            print(date)
            book = Booking(wastetype=wastetype,name=users.name,uid=users.uid ,date=date,email=users.email, booking_address=booking_address)
            book.save()
            return render(request,'dashboard/success/pickup-success.html',context=data)
        return render(request,'dashboard/pickup.html',context=data)
    else:
        data = {'status':'You need to login first'}
        return render(request,'signin.html',context=data)
    
def purchase(request):
    if 'uname' in request.session:
        data = {'name':request.session.get('uname')}
        return render(request,'dashboard/purchase.html',context=data)
    else:
        data = {'status':'You need to login first'}
        return render(request,'signin.html',context=data)
    
def report(request):
    if 'uname' in request.session:
        data = {'name':request.session.get('uname')}
        return render(request,'dashboard/report.html',context=data)
    else:
        data = {'status':'You need to login first'}
        return render(request,'signin.html',context=data)
    
def profile(request):
    if request.method == 'POST':
        user= User()
        user.name = request.POST.get('uname')
        user.email = request.POST.get('email')
        user.photo = request.FILES.get('photo')
        
        data = {'name':request.session.get('uname')}
        if user.photo:
            user.photo = request.FILES.get('photo')
        user = User(name=name,email=email,photo=user.photo)
        user.save()
        return redirect('profile')
    else:
         if 'uname' in request.session:
            name = request.session.get('uname')
            email = request.session.get('email')
            # password = {'name':request.session.get('password')}
            my_dict = {
                'name': name,
                'email':email
            }
            return render(request,'profile.html',my_dict)
         else:
            data = {'status':'You need to login first'}
            return render(request,'signin.html',context=data)


#notification
def notification(request):
    if 'uname' in request.session:
        return render(request,'notification.html')
    else:
        data = {'status':'You need to login first'}
        return render(request,'signin.html',context=data)