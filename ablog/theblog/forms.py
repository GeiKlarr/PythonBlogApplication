from django import forms
from .models import Post, Category, Comments

#choice = [('coding','coding'),('sports','sports'),('entertainment','entertainment')]
choices = Category.objects.all().values_list('name','name')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author',  'body', 'header_image')
        
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Title here'}),
          #  'title_tag': forms.TextInput(attrs={'class':'form-control'}),
            'author': forms.TextInput(attrs={'class':'form-control', 'value': '', 'id': 'poster','type':'hidden'}),
          # 'author': forms.Select(attrs={'class':'form-control'}),
           # 'category': forms.Select(choices=choices,attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}), 
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body')
        
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Title here'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('name','body')
        widgets = {
           'name': forms.TextInput(attrs={'class':'form-control','value': '','id': 'commenter','type':'hidden'}),
            'body': forms.TextInput(attrs={'class': 'form-control','placeholder':'comment here',}),
        }