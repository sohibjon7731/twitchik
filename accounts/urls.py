from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenBlacklistView
from .views import RegisterView, UsersListView, LogoutView, FollowUserView, UnfollowUserView, ListFollowingView, \
    ListFollowersView, CurrentUserView

urlpatterns = [
    path('account/login', TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('account/login/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('account/register', RegisterView.as_view(), name="sign_up"),
    path('account/logout', LogoutView.as_view(), name='user-logout'),
    path('account/current', CurrentUserView.as_view(), name='current-user'),
    path('account/users', UsersListView.as_view(), name='user-list'),

    path('follow/<int:user_id>', FollowUserView.as_view(), name='follow-user'),
    path('unfollow/<int:user_id>', UnfollowUserView.as_view(), name='unfollow-user'),
    path('following', ListFollowingView.as_view(), name='list-following'),
    path('followers', ListFollowersView.as_view(), name='list-followers'),
]
