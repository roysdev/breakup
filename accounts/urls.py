from django.urls import path
from django.contrib.auth import views as auth_views
# from .views import SignUp, AccountSecurityUpdate
from .views import SignUp


from . import views

app_name = 'account'

urlpatterns = [
    path('signup/', SignUp.as_view(), name="signup"),

    path('<username>/', views.user_profile, name="detail"),
    path('link/follow/', views.follow, name='follow'),
    path('following/<username>/', views.following_list, name='following'),
    path('followers/<username>/', views.followers_list, name='followers'),


    path('edit/profile/', views.edit_profile, name="edit"),
    path('edit/icon/', views.edit_icon, name="edit-icon"),
    path('edit/email/', views.edit_email, name="edit-email"),





]
