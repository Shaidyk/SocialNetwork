from django.shortcuts import render

from SocialNetwork.models.profile import Profile


def profile(request):
    profile = Profile.objects.all()
    print(profile)
    return render(request, 'html/main.html', context={'users': profile})
