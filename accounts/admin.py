from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin
from django.contrib.admin.views.main import ChangeList


class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name', 'is_staff', 'is_active', 'is_admin', 'date_joined', 'last_login')
    list_display_link = ('email', 'first_name', 'last_name')
    readonly_fields = ('date_joined', 'last_login')
    ordering = ('-date_joined',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

    def get_changelist(self, request, **kwargs):
        return CustomChangeList
        
    class meta:
        admin.site.site_title="Belnu Admin"
        admin.site.site_header="Belnu - Pedidos Web"
        admin.site.index_title="Administración"
  
class CustomChangeList(ChangeList):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title = 'Belnu Administración'  

# Register your models here.
admin.site.register(Account, AccountAdmin)

