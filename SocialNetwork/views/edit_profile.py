from django.shortcuts import render, redirect

from SocialNetwork.forms import UploadForm
from SocialNetwork.models.profile import Profile
from SocialNetwork.models.photo import Photo


def edit_profile_view(request):
    if not request.user.is_authenticated:
        return redirect('authenticate')
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            profile = Profile.objects.get(user=request.user)

            profile.photo.create(
                title=form.cleaned_data.get('title'),
                image=form.cleaned_data.get('image'),
                description=form.cleaned_data.get('description'),
                is_avatar=form.cleaned_data.get('is_avatar')
            )
            form.save()
            return redirect('main')
    else:
        form = UploadForm()
    return render(request, 'html/edit_profile.html', context={'form': form})
