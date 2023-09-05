from django.urls import path
from .views import CreateProfilePageView,FollowView,ShowProfilePageView,UserRegisterView, UserEditView, PasswordsChangeView, AddProfileView,CreateProfile
from django.contrib.auth import views as auth_views #this allows us to see view from auth.
from . import views

app_name = 'members'
urlpatterns = [
    path('register/',UserRegisterView.as_view(), name="register"),
    path('edit_profile/',UserEditView.as_view(), name="update_profile"),
    #path('password/',auth_views.PasswordChangeView.as_view(template_name='registration/change_password.html')),
    path('password/',PasswordsChangeView.as_view(template_name='registration/change_password.html'),name="change_password"),
    path('password_success',views.password_success, name="password_success"),
    path('edit_profile/change_picture/<int:pk>/', AddProfileView.as_view(), name="change_picture"), 
    path('edit_profile/add_picture/<int:pk>/', CreateProfile.as_view(), name="add_picture"), 
    path('<int:pk>/profile/', ShowProfilePageView.as_view(), name="show_profile"), 
    path('follow/<int:pk>', FollowView, name="user_follow"), 
    path('create_profile_page/',CreateProfilePageView.as_view(), name="create_profile"),
    
    
    
  
   ] 
