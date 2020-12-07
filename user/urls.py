from django.urls import path
from .views import index,signup1,login1,userbook
urlpatterns = [
    path('',index),
    path('signup1',signup1.as_view(),name="signup1"),
    path('login1',login1.as_view(),name="login1"),
    path('user',userbook,name="p")

   # path('xero',xero1,name='xero')

]
