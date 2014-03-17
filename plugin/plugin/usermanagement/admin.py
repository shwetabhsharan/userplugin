from plugin.usermanagement.models import UserProfile
from django.contrib import admin

class UserProfileAdmin(admin.ModelAdmin):
    list_display = UserProfile._meta.get_all_field_names()

admin.site.register(UserProfile, UserProfileAdmin)