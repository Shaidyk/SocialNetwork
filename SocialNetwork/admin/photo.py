from django.contrib import admin

from SocialNetwork.models.photo import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'image',
        'is_avatar',
    ]
