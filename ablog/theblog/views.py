from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DetailView # THIS WILL DO A QUERY SET FOR US (A LIST) FROM THE DATABASE as we all as the detailView
from .models import Post, Comments, Profile
from .forms import PostForm,EditForm, CommentForm
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.models import User

# Create your views here.


# CREATE
#ClassedBasedView
class HomeView(ListView):
   model = Post  
   template_name = 'home.html' 
   ordering = ['-post_date']
   
   def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            followed_users = user.profile.follower.all()
            queryset = Post.objects.filter(author__in=followed_users)
            return queryset
        return Post.objects.none()
   success_url = reverse_lazy('post:home')
   
   def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['form'] = CommentForm(initial={'name': self.request.user.first_name})
            return context
        
   
def add_comment_view(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            # Save the comment
            comment = form.save()
            # Optionally, you can redirect to a success page or the same page
            return redirect('post:home')
    else:
        form = CommentForm()
    
    context = {'form': form}
    return render(request, 'home.html', context)
  
   
class ArticleDetailView(DeleteView):
    model = Post
    template_name = 'article_details.html' 

class AddPostView(CreateView):
    model = Post
    form_class = PostForm 
    template_name = 'add_post.html'
    
    #fields = '__all__'
    #fields = ('title','body') # these are from models

class AddCommentView(CreateView):
    model = Comments
    form_class =  CommentForm
    template_name = 'add_comment.html'
    success_url = reverse_lazy('post:home')

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    

#UPDATE

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm 
    template_name = 'update_post.html'
    #fields = ['title','title_tag', 'body']


#DELETE

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('post:home')


def Search(request):
    
    if request.method == "POST":    
        searched = request.POST['searched']
        users = User.objects.filter(username__contains=searched)  
        return render(request, 'searchbar.html', {'searched': searched, 'users': users})
    else:
        return render(request, 'searchbar.html', {})

