
from django.forms.models import BaseModelForm
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import DetailView
#from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy, reverse
from .forms import SignUpForm, EditProfileForm, PasswordChangingForm
from django.views.generic import CreateView, UpdateView
from theblog.models import Profile, Post
from .forms import ProfileChangingForm,ProfileAddFrom,ProfilePageForm


class CreateProfilePageView(CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = 'registration/create_user_profile.html'
    
    def form_valid(self,form):
        form.instance.user = self.request.user # Grab the user and make available to form
        return super().form_valid(form)

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        return super().form_valid(form)
    

def FollowView(request, pk):
    follow = get_object_or_404(Profile, id=request.POST.get('follow_id'))
    followed = False
    if follow.follower.filter(id=request.user.id).exists():
        follow.follower.remove(request.user)
        followed = False
    else:
        follow.follower.add(request.user)
        followed = True

    return HttpResponseRedirect(reverse('members:show_profile',args=[str(pk)])) 

class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self,*args, **kwargs):
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])

        follows = get_object_or_404(Profile, id=self.kwargs['pk'])
        total_followers = follows.total_followers()

        followed = False 
        if follows.follower.filter(id=self.request.user.id).exists():
            followed = True

        posts = Post.objects.filter(author=page_user.user) #pageuser.user

        context["posts"] = posts
        context["total_followers"] = total_followers
        context["page_user"] = page_user
        context["followed"] = followed  
        return context
           
    
class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    #form_class = PasswordChangingForm
    success_url = reverse_lazy('members:password_success')

def password_success(request):
    return render(request, 'registration/password_success.html', {})

class UserRegisterView(generic.CreateView):
    form_class = SignUpForm #this will handle actual forms  from django.contrib.auth.forms import UserCreationForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm #this will handle actual forms  from django.contrib.auth.forms import UserCreationForm
    template_name = 'registration/update_profile.html'
    success_url = reverse_lazy('post:home')

    def get_object(self):
        return self.request.user #this is to know which is the current logged in user and retrieve its value to the UpdateView


class AddProfileView(UpdateView):
    model = Profile
    form_class = ProfileChangingForm
    template_name = 'registration/change_pic.html'
    success_url = reverse_lazy('post:home')
    
class CreateProfile(CreateView):
    model = Profile
    form_class = ProfileAddFrom
    template_name = 'registration/add_pic.html'
    success_url = reverse_lazy('post:home')

class CreateProfileView(CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = "registration/create_user_profile_page.html"
    fields = '__all__'

    def form_valid(self,form):
        form.instance.user = self.request.user # Grab the user and make available to form
        return super().form_valid(form)
    
