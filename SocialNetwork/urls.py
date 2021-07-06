from django.contrib import admin
from django.urls import path

from SocialNetwork.views.main import main_page


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page, name='main'),
    path('news/', main_page, name='news'),
    path('message/', main_page, name='message'),
    path('friends/', main_page, name='friends'),
    path('photo/', main_page, name='photo'),
    path('video/', main_page, name='video'),
    path('channels/', main_page, name='channels'),
]
