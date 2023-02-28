
from django.contrib import admin
from .models import Post, Category,Author

class PostAdmin(admin.ModelAdmin):
    list_display = ('header', 'authorArticle','creationTime')
    list_filter = ('header', 'creationTime', 'authorArticle')
    search_fields = ('header', 'textCategory__categoryName')

admin.site.register(Post,PostAdmin)
admin.site.register(Category)
admin.site.register(Author)
