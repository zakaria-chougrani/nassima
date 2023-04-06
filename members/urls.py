from django.urls import path

from members.views import  login_view, logout_view
urlpatterns = [
    # path('users', users_list, name="users"),
    path('login', login_view, name="login"),
    # path("registre", registration_view, name="registre"),
    path('logout', logout_view, name="logout"),
    # path('profile', profile_view, name="profile"),
]
