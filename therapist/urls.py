from django.urls import path
from .views import index,signup,login1,\
    therapist_view,therapist_soc,therapist_lang,\
    therapist_issues,therapist_working_hours,therapist_special_hours,\
    therapist_techniques,blocked_slots,booking1,p,g,verification,email_verify_otp
urlpatterns = [
    path('',index,name="homepage"),
    path('signup',signup.as_view(),name="signup"),
    path('login2',login1.as_view(),name="login2"),
    path('therapistpro',therapist_view.as_view(),name='therapistpro'),
    path('therapistsoc',therapist_soc.as_view(),name='therapistsoc'),
    path('therapistlang',therapist_lang.as_view(),name='therapistlang'),
    path('therapistissue',therapist_issues.as_view(),name='therapistissue'),
    path('therapistwork',therapist_working_hours.as_view(),name='therapistwork'),
    path('therapistspecial',therapist_special_hours.as_view(),name='therapistspecial'),
    path('therapisttech',therapist_techniques.as_view(),name='therapisttech'),
    path('therapistblock',blocked_slots.as_view(),name='therablock'),
    path('booking', booking1.as_view(), name="booking"),
    path('p', p, name="p"),
    path('g',g,name="g"),
    path('emailotp',email_verify_otp,name="emailotp"),
    path('activate/<uidb64>/<token>',verification.as_view(),name="activate")

]
