from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    """
    Custom admin configuration for CustomUser model
    """
    model = CustomUser
    
    # Fields to display in the admin list view
    list_display = ('username', 'email', 'first_name', 'last_name', 'date_of_birth', 'is_staff', 'is_active')
    
    # Fields that can be filtered in the admin list view
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'date_joined')
    
    # Fields that can be searched in the admin
    search_fields = ('username', 'email', 'first_name', 'last_name')
    
    # Order users by username
    ordering = ('username',)
    
    # Define fieldsets for the user edit form
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Information', {
            'fields': ('date_of_birth', 'profile_photo'),
        }),
    )
    
    # Define fieldsets for the user creation form
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Information', {
            'fields': ('date_of_birth', 'profile_photo'),
        }),
    )

# Register the custom user model with the custom admin
admin.site.register(CustomUser, CustomUserAdmin)
