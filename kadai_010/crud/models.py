from django.db import models
from django.urls import reverse

# 5章で追加
# モデルの追加。データベースに反映するためには、マイグレーションファイルの作成とマイグレーションを行う必要あり。
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField()

    # 管理画面で表示されるモデルのインスタンス名を指定
    def __str__(self):
        return self.name
    
    # 8章で追加
    def get_absolute_url(self):
        return reverse('list')  # 名前からURLを取得する
