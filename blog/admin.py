
from django.contrib import admin
from django.contrib.auth.models import Group
from .models import post

# Register your models here.


class Postadmin(admin.ModelAdmin):
    list_display= ('title','slug','status','created_on')
    # list_filter= ('status')
    list_filter= ['status']
    search_fields= ('title','msg')

  
admin.site.register(post,Postadmin)
admin.site.unregister(Group)
admin.site.site_header='My Blogger'