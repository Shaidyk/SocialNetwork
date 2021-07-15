from django.shortcuts import redirect, render


def authenticate_view(request):
    return render(request, 'html/authenticate.html', context={})
