from django.urls import path
from .views import signup_view, login_view, logout_view, profile_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('signup/', signup_view, name='signup'),
]
