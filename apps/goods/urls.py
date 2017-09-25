from django.conf.urls import url
from goods.views import GoodsListView


urlpatterns = [
    url(r'list/', GoodsListView.as_view(), name='list')
]