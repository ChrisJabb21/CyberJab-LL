from django.contrib import admin
from CyberJab.models import Post


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_date')
    list_filter = ('status',)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)
