from django.contrib import admin
from .models import PostModel,Comment

# Register your models here.

class PostModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'creation_date')

admin.site.register(PostModel,PostModelAdmin)
admin.site.register(Comment)