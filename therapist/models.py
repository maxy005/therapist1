from django.db import models
from user.models import user
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class therapist(models.Model):


    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=12)
    created_at=models.DateField()
    password_hash=models.CharField(max_length=100)
    invite_code=models.CharField(max_length=100)
    is_valid=models.BooleanField(default=False)


    def therapist(self):
        self.save()

    @staticmethod
    def get_therapist_all():
        return therapist.objects.all()

    @staticmethod
    def get_email(email):
        try:
            return therapist.objects.get(email=email)
        except:
                return False

    def __str__(self):
        return self.first_name

    def isexists(self):
        if therapist.objects.filter(email=self.email):
            return True
        else:
            return False

class therapist_profile(models.Model):

   therapist_id=models.ForeignKey(therapist,to_field="id",on_delete=models.CASCADE,default=1,null=True)
   title=models.CharField(max_length=100)
   credentials=models.CharField(max_length=50)
   experience=models.CharField(max_length=50)
   sex=models.CharField(max_length=50)
   age=models.CharField(max_length=50)
   shortbio=models.CharField(max_length=100)
   background=models.CharField(max_length=100)
   personalbelief=models.CharField(max_length=100)
   website=models.CharField(max_length=100)

   def therapistpro(self):
       self.save()

   @staticmethod
   def get_therapist_profile_all():
       return therapist_profile.objects.all()


   def __str__(self):
        return self.title





   def therapist_profile_by_id(therapist_id):
       print(therapist_id)
       if therapist_id:
            print("hell")
            return therapist_profile.objects.filter(therapist_id=therapist_id)
       else:

           therapist_profile.therapist_profile_all();


class therapist_social_media(models.Model):
    therapist_id= models.ForeignKey(therapist, on_delete=models.CASCADE,default=None,null=True)
    facebook=models.CharField(max_length=100,default=None,null=True)
    instagram=models.CharField(max_length=100,default=None,null=True)
    linkedIn=models.CharField(max_length=100,default=None,null=True)
    twitter=models.CharField(max_length=100,default=None,null=True)
    youtube=models.CharField(max_length=100,default=None,null=True)

    def therapistsoc(self):
        self.save()



class therapist_languages(models.Model):

    therapist_id= models.ForeignKey(therapist, on_delete=models.CASCADE,default=None,null=True)
    language=models.CharField(max_length=50)
    def therapistlang(self):
        self.save()

    def __str__(self):
        return str(self.language)


class therapist_issue(models.Model):

    therapist_id= models.ForeignKey(therapist, on_delete=models.CASCADE,default=None,null=True)
    issue=models.CharField(max_length=100)
    other_issue=models.CharField(max_length=100)

    def therapistissue(self):
        self.save()

    def __str__(self):
        return str(self.issue)


class therapist_technique(models.Model):

    therapist_id= models.ForeignKey(therapist, on_delete=models.CASCADE,default=None,null=True)
    technique=models.CharField(max_length=100)

    def therapisttech(self):
        self.save()

    def __str__(self):
        return str(self.technique)


class therapist_working_hour(models.Model):

    therapist_id= models.ForeignKey(therapist, on_delete=models.CASCADE,default=None,null=True)
    starttime=models.TimeField(null=True, blank=True)
    endtime=models.TimeField(null=True, blank=True)
    rate=models.CharField(max_length=40)

    def therapistwork(self):
        self.save()

    def __str__(self):
        return str(self.starttime)




    @staticmethod
    def get_therapist_working_all():
        return therapist_working_hour.objects.all()

    @staticmethod
    def therapist_working_by_id(therapist_id2):
        return therapist_working_hour.objects.filter(therapist_id=therapist_id2)

class therapist_special_hour(models.Model):

    therapist_id= models.ForeignKey(therapist, on_delete=models.CASCADE,default=None,null=True)
    starttime=models.CharField(max_length=50,null=True, blank=True)
    endtime=models.CharField(max_length=50,null=True, blank=True)
    day=models.CharField(max_length=50,null=True,blank=True)

    def therapistspecial(self):
        self.save()

    def __str__(self):
        return str(self.starttime)

class blocked_slot(models.Model):

    therapist_id= models.ForeignKey(therapist, on_delete=models.CASCADE,default=None,null=True)
   # user1=models.ForeignKey(user,on_delete=models.CASCADE,default=None,null=True)
    #therapist1=models.ForeignKey(therapist_working_hour,on_delete=models.CASCADE,default=None,null=True)
    starttime = models.CharField(max_length=50,null=True,blank=True)
    endtime = models.CharField(max_length=50,null=True,blank=True)

    def therapistblock(self):
        self.save()

    def __str__(self):
        return str(self.starttime)


class session_tab(models.Model):
    user_id=models.ForeignKey(user,on_delete=models.CASCADE),
    therapist_id=models.ForeignKey(therapist,on_delete=models.CASCADE)
    start_session=models.CharField(max_length=100)
    end_session=models.CharField(max_length=100)

class booking(models.Model):
    therapist_id=models.ForeignKey(therapist,on_delete=models.CASCADE)
    starttime=models.CharField(max_length=50,null=True)
    endtime=models.CharField(max_length=50,null=True)

    def nis(self):
        self.save()

    def __str__(self):
        return str(self.starttime)


class otp(models.Model):
    therapist_id = models.ForeignKey(therapist, on_delete=models.CASCADE)
    time_st=models.DateTimeField(auto_now=True)
    emailotp=models.SmallIntegerField()

    def __str__(self):
        return str(self.emailotp)