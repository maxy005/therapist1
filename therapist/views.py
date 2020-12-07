from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import therapist,therapist_profile,therapist_social_media,therapist_issue,therapist_technique,therapist_special_hour,therapist_languages,therapist_working_hour,blocked_slot,booking
from django.contrib.auth.hashers import make_password,check_password
from datetime import datetime
from django.utils import timezone
from django.views import View
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMessage
from django.urls import reverse
from django.utils.encoding import force_bytes,force_text, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from .utils import token_generator
import random

import time,datetime
# Create your views here.
def index(request):
    return render(request,'index.html')

class signup(View):

    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        #print(first_name,last_name,phone,email,password)
        # validations
        error_message=None
        th=therapist(
            first_name = first_name,
            last_name = last_name,
            phone=phone,
            email =email,
            password_hash =make_password(password),
            created_at=timezone.now(),
            is_valid = False
        )

        isexists =th.isexists()
        print(th.is_valid)
        print("here the therapist is false vadu thay che !......")
        th.therapist()

        if isexists:
            error_message='Email Already Exists: '
        if (not error_message):
            print(first_name, last_name, phone, email, password)
            #password1=make_password(password)

           # th.therapist()
            uidb64 = urlsafe_base64_encode(force_bytes((th.pk)))
            domain = get_current_site(request).domain

            # domain=get_current_site(request).domain
            '''aa email link sending for verification is done from youtube https://www.youtube.com/watch?v=e3UhXKVECPI&ab_channel=SemyColon'''
            link = reverse("activate", kwargs={'uidb64': uidb64, 'token': token_generator.make_token(th)})
            activate_url = "http://" + domain + link
            otp=random.randint(100000,999999)

            email_body = "hi " + th.first_name + " please click the link \n" + activate_url
            email = EmailMessage(
                "Account Created",
                email_body,

                "max.chawdabuisness@gmail.com",
                [email],

            )

            email.send(fail_silently=False)
            if th is not None and token_generator.check_token(th, token_generator.make_token(th)):
                print(" here only the therapist is created ...")

                th.is_valid = True
                th.therapist()
                login1()
            return redirect("homepage")

        else:
            data = {
                'error': error_message,
                }

            return render(request, 'signup.html', data)

    def get(self,request):
        return render(request,'signup.html')

class verification(View):
    def get(self,request,uidb64,token):
        return redirect("login2")

class email_verify_otp(View):
    def post(self,request):
        pass

class login1(View):

    def post(self,request):
        postdata=request.POST
        email=postdata.get('email')
        password=postdata.get('password')
        therapist1=therapist.get_email(email)
        error_message=None
        if therapist1:
            c=check_password(password,therapist1.password_hash)
            if c :
                request.session['therapist1.e']=therapist1.email
                request.session['therapist1.p']=therapist1.password_hash
                print(request.session.get('therapist1.e'))
                print(request.session.get('therapist1.p'))
                print(therapist1.id)
                return redirect("therapistpro")
            else:
                error_message="Invalid password !"
                return render(request,'login1.html',{'error':error_message})
        error_message = " Invalid Email "
        return render(request,'login1.html',{'error':error_message})

    def get(self,request):
        return render(request,'login1.html')

class therapist_view(View):
  def post(self,request):
    postData = request.POST
    current_email =  request.session.get('therapist1.e')
    print(current_email, "Currently logged in email")
    current_therapist = therapist.get_email(current_email)
    print(current_therapist, "Currently logged in name")
    therapist_id=therapist.objects.get(id=current_therapist.id)
    #therapist_id=current_therapist.id
    print(therapist_id, "<- therapist id")

    title = postData.get('title')
    credentials = postData.get('credentials')
    experience= postData.get('experience')
    sex = postData.get('sex')
    age = postData.get('age')
    shortbio=postData.get('shortbio')
    background=postData.get('background')
    personalbelief=postData.get('personalbelief')
    website=postData.get('website')
    print(title,credentials,sex,age,experience,shortbio,background,personalbelief)
    th1=therapist_profile(
        title=title,
        credentials=credentials,
        experience=experience,
        therapist_id=therapist_id,
        sex=sex,
        age=age,
        shortbio=shortbio,
        background=background,
        personalbelief=personalbelief,
        website=website
    )
    th1.therapistpro()
    print("profile created")

    return redirect("therapistsoc")

  def get(self,request):
      return render(request,'therapistpro.html')


class therapist_soc(View):
    def post(self,request):
        postData = request.POST
        current_email = request.session.get('therapist1.e')
        print(current_email, "Currently logged in email")
        current_therapist = therapist.get_email(current_email)
        print(current_therapist, "Currently logged in name")
        therapist_id = therapist.objects.get(id=current_therapist.id)
        # therapist_id=current_therapist.id
        print(therapist_id, "<- therapist id")
        facebook = postData.get('facebook')
        instagram = postData.get('instagram')
        linkedIn = postData.get('linkedIn')
        twitter = postData.get('twitter')
        youtube = postData.get('youtube')
        print(facebook,instagram,linkedIn,twitter,youtube)
        th2=therapist_social_media(
            therapist_id=therapist_id,
            facebook=facebook,
            instagram=instagram,
            linkedIn=linkedIn,
            twitter=twitter,
            youtube=youtube
        )
        th2.therapistsoc()
        print("created social media")
        return redirect('therapistlang')

    def get(self,request):
        return render(request,'therapistsoc.html')

class therapist_lang(View):
    def post(self,request):
        postData = request.POST
        current_email = request.session.get('therapist1.e')
        print(current_email, "Currently logged in email")
        current_therapist = therapist.get_email(current_email)
        print(current_therapist, "Currently logged in name")
        therapist_id = therapist.objects.get(id=current_therapist.id)
        # therapist_id=current_therapist.id
        print(therapist_id, "<- therapist id")
        language=postData.get('language')
        print(language)
        th2 = therapist_languages(
            therapist_id=therapist_id,
            language=language,
        )

        th2.therapistlang()
        print("language")
        return redirect("therapistissue")

    def get(self,request):
        return render(request, 'therapistlang.html')


class therapist_issues(View):
    def post(self,request):
        postData = request.POST
        current_email = request.session.get('therapist1.e')
        print(current_email, "Currently logged in email")
        current_therapist = therapist.get_email(current_email)
        print(current_therapist, "Currently logged in name")
        therapist_id = therapist.objects.get(id=current_therapist.id)
        # therapist_id=current_therapist.id
        print(therapist_id, "<- therapist id")
        issue=postData.get('issue')
        other_issue=postData.get('otherissue')
        print(issue)
        print(other_issue)
        th3 = therapist_issue(
            therapist_id=therapist_id,
            issue=issue,
            other_issue=other_issue

        )
        th3.therapistissue()
        print("saved issues")
        return redirect("therapisttech")

    def get(self,request):
        return render(request, 'therapistissue.html')


class therapist_techniques(View):
    def post(self,request):
        postData = request.POST
        current_email = request.session.get('therapist1.e')
        print(current_email, "Currently logged in email")
        current_therapist = therapist.get_email(current_email)
        print(current_therapist, "Currently logged in name")
        therapist_id = therapist.objects.get(id=current_therapist.id)
        # therapist_id=current_therapist.id
        print(therapist_id, "<- therapist id")
        technique=postData.get('technique')
        th4 = therapist_technique(
            therapist_id=therapist_id,
            technique=technique,
        )
        th4.therapisttech()
        print("saved technique")
        return redirect("therapistwork")
    def get(self,request):
        return render(request, 'therapisttechnique.html')


class therapist_working_hours(View):
    def post(self,request):
        postData = request.POST
        current_email = request.session.get('therapist1.e')
        print(current_email, "Currently logged in email")
        current_therapist = therapist.get_email(current_email)
        print(current_therapist, "Currently logged in name")
        therapist_id = therapist.objects.get(id=current_therapist.id)
        # therapist_id=current_therapist.id
        print(therapist_id, "<- therapist id")
        starttime=postData.get('starttime')
        endtime=postData.get('endtime')
        rate=postData.get('rate')

        #timestamp=starttime
        #dt=datetime.fromtimestamp(timestamp)
        #print(dt)


        th5 = therapist_working_hour(
            therapist_id=therapist_id,
            starttime=starttime,
            endtime=endtime,
            rate=rate

        )
        th5.therapistwork()
        print(starttime)
        print("saved working hours")
        return redirect("therapistspecial")
    def get(self,request):
        return render(request, 'therapistworking.html')

class therapist_special_hours(View):
    def post(self,request):
        postData = request.POST
        current_email = request.session.get('therapist1.e')
        print(current_email, "Currently logged in email")
        current_therapist = therapist.get_email(current_email)
        print(current_therapist, "Currently logged in name")
        therapist_id = therapist.objects.get(id=current_therapist.id)
        # therapist_id=current_therapist.id
        print(therapist_id, "<- therapist id")
        starttime = postData.get('starttime')
        endtime = postData.get('endtime')
        day= postData.get('day')

        print(starttime)
        print(endtime)
        print(day)

        th6 = therapist_special_hour(
            therapist_id=therapist_id,
            starttime=starttime,
            endtime=endtime,
            day=day

        )
        th6.therapistspecial()
        print("saved special hours")
        return redirect("therablock")
    def get(self,request):
        return render(request, 'therapistspecial.html')

class blocked_slots(View):
    def post(self,request):
        postData = request.POST
        current_email = request.session.get('therapist1.e')
        print(current_email, "Currently logged in email")
        current_therapist = therapist.get_email(current_email)
        print(current_therapist, "Currently logged in name")
        therapist_id = therapist.objects.get(id=current_therapist.id)
        # therapist_id=current_therapist.id
        print(therapist_id, "<- therapist id")
        starttime = postData.get('starttime')
        endtime = postData.get('endtime')


        print(starttime)
        print(endtime)


        th7 = blocked_slot(
            therapist_id=therapist_id,
            starttime=starttime,
            endtime=endtime


        )
        th7.therapistblock()
        print("saved blocked slot")
        return redirect("homepage")
    def get(self,request):
        return render(request, 'therapistblocked.html')

class booking1(View):
    def post(self,request):
        postData = request.POST
        current_email = request.session.get('therapist1.e')
        print(current_email, "Currently logged in email")
        current_therapist = therapist.get_email(current_email)
        print(current_therapist, "Currently logged in name")
        therapist_id = therapist.objects.get(id=current_therapist.id)
        # therapist_id=current_therapist.id
        print(therapist_id, "<- therapist id")
        starttime = postData.get('starttime')
        endtime= postData.get('endtime')
        #day = postData.get('day')



        th7 = booking(
            therapist_id=therapist_id,
            starttime=starttime,
            endtime=endtime,


        )
        th7.nis()
        print(starttime)
        print(endtime)

        print("saved booking hours")
        return redirect("booking")

    def get(self,request):
        return render(request, 'booking.html')

def p(request):

    thera=therapist.get_therapist_all()

    therapistpro=None
    categoryid = request.GET.get('x')

    print(categoryid, 'this is the category ids')

    if categoryid:

        therapistpro = therapist_profile.therapist_profile_by_id(categoryid)
        print(therapistpro, 'this is therapistprofile')

    else:
        thera= therapist.get_therapist_all()
        print('it is else part')

    data = {}
    data['therapistpro'] = therapistpro
    data['thera'] = thera
    return render(request,'p.html',data)

def g(request):
    therapistorig=therapist.get_therapist_all()
