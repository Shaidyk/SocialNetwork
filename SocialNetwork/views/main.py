from django.shortcuts import render, redirect
from django.contrib.auth import authenticate

from SocialNetwork.models.profile import Profile, FriendRequest


def main_page_view(request):
    if not request.user.is_authenticated:
        return redirect('authenticate')
    if request.user.is_authenticated:
        all_friend_requests = FriendRequest.objects.filter(to_user=request.user)
        profile = Profile.objects.get(user=request.user)
        return render(request,
                      'html/main.html',
                      context={
                          'user': profile,
                          'all_friend_requests': all_friend_requests,
                      })
    return render(request, 'html/main.html', context={})
