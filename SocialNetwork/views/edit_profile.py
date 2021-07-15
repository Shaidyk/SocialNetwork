from django.shortcuts import render, redirect

from SocialNetwork.forms import UploadForm
from SocialNetwork.models.profile import Profile


def edit_profile_view(request):
    if not request.user.is_authenticated:
        return redirect('authenticate')
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            profile = Profile.objects.get(user=request.user)
            profile.photo = form.cleaned_data.get('image')
            form.save()
            return redirect('main')
    else:
        form = UploadForm()
    return render(request, 'html/edit_profile.html', context={'form': form})
