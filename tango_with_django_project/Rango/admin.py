from django.contrib import admin

from Rango.models import Category, Page
from django.utils.html import escape

# admin.site.register(Category)
# admin.site.register(Page)


class PageAdmin(admin.ModelAdmin):
    # fields = ['title', 'category', 'url']
    list_display = ('title', 'category', 'url')
    fieldsets = (('hello', {'fields': ('url',), 'description': escape('hello world')}), ('world', {'fields': ('category', 'url'), 'classes': ('collapse',), 'description': 'hi i am xiao yun liu'}),) #  escape负责转义
    # fields = ('url', 'title', 'category')
    empty_value_display = '__empty__'


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}  # 在添加新的Category时，填写slug字段最好是自动填充，因为当有空格时需要用链接符‘-’链接，并且大写转小写


admin.site.register(Page, PageAdmin)
admin.site.register(Category, CategoryAdmin)