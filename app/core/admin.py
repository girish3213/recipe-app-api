"""
Django admin customizations
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from core import models
from django.utils.translation import gettext_lazy as _

class UserAdmin(BaseUserAdmin):
    """Define admin model for custom user model"""
    ordering = ['id']
    list_display = ['email', 'name']
    # This will display the email and name fields in the list users page
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        # This will display the email and password fields in the add user page
        # and the change user page
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active', 
                    'is_staff', 
                    'is_superuser',
                    )
            }
        ),
        (_('Important dates'), {'fields': ('last_login',)}),
        # This will display the last login field in the add user page
        # and the change user page
        
    )
    readonly_fields = ['last_login',] 
    add_fieldsets = (
        (None, {
            #'classes': ('wide',),
            'fields': (
                'email', 
                'password1', 
                'password2',
                'name',
                'is_active',
                'is_staff',
                'is_superuser',
                )
        }),
        # This will display the email, password1 and password2 fields in the
        # add user page
    )
      
    
    
    
admin.site.register(models.User, UserAdmin)
admin.site.register(models.Recipe)