from django.contrib import admin

from .models import emp_salary,emp_table
from django.contrib.admin.sites import AlreadyRegistered
from django.apps import apps
from django.utils.html import format_html

class emp_Admin(admin.ModelAdmin):
    list_display= ('emp_id', 'emp_first_name', 'emp_last_name',)

class emp_sal_admin(admin.ModelAdmin):
    list_display= ('id1', 'emp_sal')

def click_me(self,obj):
    return format_html('<button class="default> view </button>') 


admin.site.register(emp_salary)
admin.site.register(emp_table,emp_Admin)





