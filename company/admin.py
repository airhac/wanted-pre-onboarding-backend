from django.contrib import admin
from .models import Company
from .models import User
# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('company_id', 'company_name')
    
admin.site.register(Company, CompanyAdmin)

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_name')
    
admin.site.register(User, UserAdmin)