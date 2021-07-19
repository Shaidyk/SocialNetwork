from django.shortcuts import render, redirect

from SocialNetwork.models.profile import Profile


def photo_view(request):
    if not request.user.is_authenticated:
        return redirect('authenticate')
    profile = Profile.objects.get(user=request.user)
    photo = profile.photo.all()

    return render(request, 'html/photo.html', context={'photos': photo})
