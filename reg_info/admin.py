from django.contrib import admin
from reg_info.models import RegInfo

class RegInfoAdmin(admin.ModelAdmin):
    list_display=('firstname','lastname','email','password','conf_password','sel_deg','pos','grad_year')

admin.site.register(RegInfo,RegInfoAdmin)


