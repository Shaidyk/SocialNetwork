from django.shortcuts import render, redirect
from django.contrib.auth import authenticate

from SocialNetwork.models.profile import Profile, FriendRequest


def main_page_view(request):
    if not request.user.is_authenticated:
        return redirect('authenticate')
    if request.user.is_authenticated:
        all_friend_requests = FriendRequest.objects.filter(to_user=request.user)
        profile = Profile.objects.get(user=request.user)
        photos = profile.photo.all()
        avatar = None
        for photo in photos:
            if photo.is_avatar:
                avatar = photo
                break

        return render(request,
                      'html/main.html',
                      context={
                          'user': profile,
                          'avatar': avatar,
                          'all_friend_requests': all_friend_requests,
                      })
    return render(request, 'html/main.html', context={})
