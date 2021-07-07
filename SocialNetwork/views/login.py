from django.contrib.auth import login, authenticate
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm

from SocialNetwork.forms import LoginForm


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('main')
    else:
        form = AuthenticationForm()
    return render(request, 'html/login.html', {'form': form})

