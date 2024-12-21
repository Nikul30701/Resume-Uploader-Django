from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from resume_uploader_12.models import Resume


# Unregister the built-in User model
admin.site.unregister(User)

@admin.register(Resume)
class ResumeModelAdmin(admin.ModelAdmin):
    list_display = ('id','name','role')
    list_filter = ('skill','role')
    search_fields = ('skill','name')

