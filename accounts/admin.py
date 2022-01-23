from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account
from django_jalali.admin.filters import JDateFieldListFilter

# Register your models here.

class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active')
    list_display_links = ('email', 'first_name', 'last_name')
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined',)

    filter_horizontal = ()
    list_filter = (
        ('date_joined', JDateFieldListFilter),
    )
    fieldsets = ()

admin.site.register(Account, AccountAdmin)
