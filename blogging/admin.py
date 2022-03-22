from django.contrib import admin
from blogging.models import Post, Category


class CategoryTabularInline(admin.TabularInline):
    model = Category.posts.through


class PostAdmin(admin.ModelAdmin):
    inlines = [CategoryTabularInline]

    class Meta:
        model = Post


class CategoryAdmin(admin.ModelAdmin):
    exclude = ("posts",)


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
