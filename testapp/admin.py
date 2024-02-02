from django.contrib import admin

from .models import CRM

class AdminCRM(admin.ModelAdmin):
    list_display = ['id','created_at','first_name','last_name','email','phone','address','zipcode']

admin.site.register(CRM,AdminCRM)