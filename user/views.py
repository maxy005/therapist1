
from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password,check_password
from django.http import HttpResponse
from .models import user
from therapist.models import therapist,therapist_working_hour
from django.views import View
from django.core.mail import send_mail

from django.utils import timezone
# Create your views here.

def index(request):

    return render(request,'index.html')

class signup1(View):

    def post(self,request):


        postData = request.POST
        first_name = postData.get('firstname')

        last_name = postData.get('lastname')
        phone = postData.get('phone')
        date=postData.get('date')
        password = postData.get('password')

        print(first_name,last_name,phone,password)

        # validations
        error_message=None
        th=user(
            first_name = first_name,
            last_name = last_name,
            phone=phone,
            #date=date,
            password = make_password(password)


        )
        j=th.isexists()
        if j:
            print("phone is there !")
            error_message="Phone Already Exists"
        if (not error_message):
            print(first_name, last_name, phone, password)
            # password1=make_password(password)
            th.user()

            print("created")
            return redirect("/login1")
        else:
            return render(request, 'signup1.html',{'error':error_message})

    def get(self,request):

        return render(request,'signup1.html')

class login1(View):

    def post(self, request):
        postdata=request.POST
        phone=postdata.get('phone')
        password=postdata.get('password')
        user1=user.get_phone(phone)
        error_message=None
        if user1:
            c=check_password(password,user1.password)
            if c:


                request.session['user.phone']=user1.phone
                print("this is the user"+request.session.get("user.phone"))
                return redirect("/p")
            else:
                error_message="invalid password !"
                print("it is else in user")
                return render(request,'login.html',{'error':error_message})
        else:
            error_message="invalid phone number"
            print("it is else in user")
            return render(request,'login.html',{'error':error_message})

    def get(self,request):
        return render(request,'login.html')



def userbook(request):
    return redirect("/p")

