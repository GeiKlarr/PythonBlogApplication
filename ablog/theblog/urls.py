from django.urls import path
#from . import views
from .views import Search,HomeView,ArticleDetailView,AddPostView,UpdatePostView,DeletePostView,AddCommentView
from . import views
app_name = 'post'
urlpatterns = [
   # path('',views.home,name="home"),
   path('',HomeView.as_view(), name="home"),  #.as_view() we use this because we're using class based view
   path('article/<int:pk>',ArticleDetailView.as_view(), name="article-detail"),
   path('add_post/', AddPostView.as_view(), name="add_post"),
   path('article/edit/<int:pk>', UpdatePostView.as_view(), name="update_post"),
   path('article/<int:pk>/delete', DeletePostView.as_view(), name="delete_post"),
   path('<int:pk>/add_comment/', AddCommentView.as_view(), name="add_comment"),
  # path('follow/<int:pk>/', views.follow, name='follow'),
   path('search/', Search, name="search_user"),
     path('add-comment/', views.add_comment_view, name='add_comment'),
   ]
