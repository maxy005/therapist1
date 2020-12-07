from django.contrib import admin
from .models import therapist,therapist_issue,therapist_languages,therapist_profile,therapist_social_media,therapist_special_hour,therapist_technique,therapist_working_hour,blocked_slot,session_tab,booking,otp


# Register your models here.
admin.site.register(therapist)
admin.site.register(therapist_profile)
admin.site.register(therapist_languages)
admin.site.register(therapist_issue)
admin.site.register(therapist_working_hour)
admin.site.register(therapist_special_hour)
admin.site.register(therapist_social_media)
admin.site.register(therapist_technique)
admin.site.register(blocked_slot)
admin.site.register(session_tab)
admin.site.register(booking)
admin.site.register(otp)