from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Product
from django.urls import reverse_lazy

# 4章で追加
class TopView(TemplateView):
    template_name = "top.html"

# 6章で追加
# ListViewは一覧画面の実装向け
class ProductListView(ListView):
    model = Product
    paginate_by = 3     # ページネーションを有効化。page_objがテンプレートへ渡され利用可能になる。
    #template_name = "" # ListViewを継承した場合、Template名はデフォルトでModel名_list.htmになる。template_nameで任意の指定も可能。

# 8章で追加
# データを追加するView
class ProductCreateView(CreateView):
    model = Product
    fields = '__all__'

# 9章で追加
# データを編集するView
class ProductUpdateView(UpdateView):
    model = Product
    fields = '__all__'
    template_name_suffix = '_update_form'

# 10章で追加
# データを削除するView
class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('list')

# 課題で追加
class ProductDetailView(DetailView):
    model = Product