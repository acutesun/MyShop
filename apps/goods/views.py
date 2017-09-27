from rest_framework import generics, mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from goods.filters import GoodsFilter
from goods.models import Goods
from goods.serializers import GoodsSerializer


class GoodsPagination(PageNumberPagination):
    '''
    分页
    '''
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 100


class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    '''
        商品列表页, 分页, 过滤, 搜索, 排序
    '''
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination  # 使用自定义的class对列表分页
    filter_class = GoodsFilter  # 过滤

    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    search_fields = ('name', 'goods_brief')
    ordering_fields = ('add_time', )


