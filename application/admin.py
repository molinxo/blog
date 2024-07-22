from django.contrib import admin
from application.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_at',)
    list_filter = ('status',)
    search_field = ('title', 'content',)


admin.site.register(Post, PostAdmin)




# Register your models here.
