from django.contrib import admin
from accounts.models import ProfileModel

# Register your models here.

class ProfileModelAdmin(admin.ModelAdmin):
    list_display = ['phone', 'user']
    # list_filter = ['gender']
    search_fields = ['phone']


admin.site.register(ProfileModel, ProfileModelAdmin)
