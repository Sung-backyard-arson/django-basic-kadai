from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Product, Category

# 5章で追加
# モデルの管理画面をカスタムするクラス。
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name','price','category','image')    # 管理画面に表示するフィールドを指定する。
    search_fields = ('name',)                                   # 管理画面に検索BOXを追加し、検索対象のフィールドを指定する。
    list_filter = ('category',)                                 # 絞り込みの機能を追加。

    # 12章で追加
    def image(self, obj):
        return mark_safe('<img src="{}" style="width:100px height:auto;">'.format(obj.img.url))

# 11章で追加
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    search_fields = ('name',)

# 管理画面に登録
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
