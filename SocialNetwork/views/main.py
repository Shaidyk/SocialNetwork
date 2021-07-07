from django.shortcuts import render
from django.contrib.auth import authenticate

from SocialNetwork.models.profile import Profile


def main_page_view(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        return render(request, 'html/main.html', context={'user': profile})
    return render(request, 'html/main.html', context={})
