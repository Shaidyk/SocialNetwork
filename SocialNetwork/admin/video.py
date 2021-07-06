from django.contrib import admin

from SocialNetwork.models.video import Video


@admin.register(Video)
class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        'title',
    ]