from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# admin.site.register(User, UserAdmin)

# modificar el admin de django para que muestre los campos que queremos
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'avatar', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')
    
    fieldsets = (
        (None, {'fields': ('avatar', 'username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Extra info', {'fields': ('roll', 'ip')}),
    )