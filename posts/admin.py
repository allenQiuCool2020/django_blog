from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "updated", "timestamp"]
    list_display_links = ["updated"]
    list_filter = ["updated", "timestamp"]
    list_editable = ["title"]
    search_fields = ["content"]
    class Meta:
        model = Post

# Register your models here.

admin.site.register(Post, PostAdmin)