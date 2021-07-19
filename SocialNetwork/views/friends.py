from django.shortcuts import render, redirect

from SocialNetwork.models.profile import Profile


def friends_view(request):
    if not request.user.is_authenticated:
        return redirect('authenticate')
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        friend_list = profile.friends.all()
        print(friend_list)
        for friend in friend_list:
            print(friend.profile.photo)
            # photos = friend.photo.all()
            # for photo in photos:
            #     print(photo)

        return render(request,
                      'html/friends.html',
                      context={
                          'friend_list': friend_list,
                      })
    return render(request, 'html/main.html', context={})
