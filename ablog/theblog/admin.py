from django.contrib import admin
from .models import Post,Category,Profile,Comments, Follow

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(Comments)
admin.site.register(Follow)