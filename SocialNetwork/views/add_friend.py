from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate

from SocialNetwork.models.profile import Profile, FriendRequest


@login_required
def send_request_user(request, userID):
    from_user = request.user
    to_user = Profile.objects.get(user__id=userID)
    friend_request, create = FriendRequest.objects.get_or_create(from_user=from_user, to_user=to_user.user)
    if create:
        return render(request, 'html/request_sent.html', context={})
    else:
        return render(request, 'html/request_was_sent.html', context={})


@login_required
def accept_friend_request(request, requestID):
    friend_reques = FriendRequest.objects.get(id=requestID)
    if friend_reques.to_user == request.user:
        friend_reques.to_user.friends.add(friend_reques.from_user.profile)
        friend_reques.from_user.friends.add(friend_reques.to_user.profile)
        friend_reques.delete()
        return HttpResponse('Request accept')
    else:
        return HttpResponse('Request decline')


def all_users(request):
    profile = Profile.objects.all().exclude(user__id=request.user.id)
    return render(request, 'html/all.html', context={'users': profile})
