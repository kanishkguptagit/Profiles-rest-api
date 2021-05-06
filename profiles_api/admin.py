from django.contrib import admin
from profiles_api import models

# Register your models here.

class UserProfileShow(admin.ModelAdmin):
    list_display = ('email','name')

admin.site.register(models.UserProfile, UserProfileShow)

admin.site.register(models.ProfileFeedItem)