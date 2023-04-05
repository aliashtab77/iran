from django.contrib import admin
from yami.models import Product, Category
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'is_pub']
    list_filter = ['price', 'is_pub']
    search_fields = ['title']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
