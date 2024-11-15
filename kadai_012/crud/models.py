from django.db import models
from django.urls import reverse

# モデルの追加しデータベースに反映するためには、マイグレーションファイルの作成とマイグレーションを行う必要あり。

# 11章で追加
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
        
# 5章で追加
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)        # 11章で追加。「1：多」のリレーションを設定する。
    img = models.ImageField(blank=True, default='noImage.png')              # 12章で追加。
    description = models.TextField(max_length=500, blank=True, null=True)   # 課題12で追加


    # 管理画面で表示されるモデルのインスタンス名を指定
    def __str__(self):
        return self.name
    
    # 8章で追加
    # モデルインスタンスの情報に基づきリダイレクトさせたい場合はget_absolute_urlを使う？
    # Viewにsuccess_urlを指定しない場合はget_absolute_urlが呼ばれるので、現状では商品の追加・編集共通でここが呼ばれる。
    def get_absolute_url(self):
        return reverse('list')  # 名前からURLを取得する
        #return reverse('detail', kwargs={'pk' : self.pk})   # こうすると商品の詳細ページへリダイレクトできる。

