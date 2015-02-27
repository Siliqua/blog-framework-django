from django.contrib import admin
from blog.models import Blog, Categoria

class BlogAdmin(admin.ModelAdmin):
    exclude = ['posted']
    prepopulated_fields = {'slug': ('titulo',)}

class CategoriaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('titulo',)}

admin.site.register(Blog)
admin.site.register(Categoria)