from django.shortcuts import render, redirect

from SocialNetwork.models.profile import Profile


def friends_view(request):
    if not request.user.is_authenticated:
        return redirect('authenticate')
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        friend_list = profile.friends.select_related()
        return render(request,
                      'html/friends.html',
                      context={
                          'friend_list': friend_list,
                      })
    return render(request, 'html/main.html', context={})
