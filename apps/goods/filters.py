from django_filters import rest_framework as filters
from goods.models import Goods
import django_filters


class GoodsFilter(filters.FilterSet):
    min_price = django_filters.NumberFilter(name="shop_price", lookup_expr='gte')
    max_price = django_filters.NumberFilter(name="shop_price", lookup_expr='lte')

    class Meta:
        model = Goods
        fields = ['min_price', 'max_price']