from django.contrib import admin
from .models import Product

# 5章で追加
# モデルの管理画面をカスタムするクラス。
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name','price')    # 管理画面に表示するフィールドを指定する。
    search_fields = ('name',)               # 管理画面に検索BOXを追加し、検索対象のフィールドを指定する。

# 管理画面に登録
admin.site.register(Product, ProductAdmin)