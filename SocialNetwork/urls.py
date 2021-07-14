from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from SocialNetwork.views.main import main_page_view
from SocialNetwork.views.register import register_view
from SocialNetwork.views.login import login_view
from SocialNetwork.views.logout import logout_view
from SocialNetwork.views.edit_profile import edit_profile_view
from SocialNetwork.views.add_friend import send_request_user, accept_friend_request, all_users


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page_view, name='main'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('edit/', edit_profile_view, name='edit'),
    path('all/', all_users, name='all_users'),
    path('send_request_user/<int:userID>/', send_request_user, name='send_request_user'),
    path('accept_friend_request/<int:requestID>/', accept_friend_request, name='accept_friend_request'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
