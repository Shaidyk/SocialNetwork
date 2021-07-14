from django.contrib import admin

from SocialNetwork.models.profile import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        'first_name',
        'last_name',
        'nick',
        'email',
    ]

    filter_horizontal = [
        'friends'
    ]
