from django.shortcuts import render
from django.contrib.auth import authenticate

from SocialNetwork.models.profile import Profile, FriendRequest


def main_page_view(request):
    if request.user.is_authenticated:
        all_friend_requests = FriendRequest.objects.all()
        profile = Profile.objects.get(user=request.user)
        return render(request,
                      'html/main.html',
                      context={
                          'user': profile,
                          'all_friend_requests': all_friend_requests,
                      })
    return render(request, 'html/main.html', context={})
