from django.contrib import admin
from django.contrib.auth.admin import UserAdmin #to add functionalities to the custom user
from .models import Account

class AccountAdmin(UserAdmin):
    list_display = ['email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active'] #data to be displayed on the table of accounts
    list_display_links = ('email', 'first_name','last_name') # add link to the first name and last name
    readonly_fields = ('last_login', 'date_joined') # read only to last login and date joined
    ordering = ('-date_joined',) # ordering by date of joining

    filter_horizontal = ()
    list_filter = ()
    fieldsets = () # read only password of custom users

admin.site.register(Account, AccountAdmin)
