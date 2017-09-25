from goods.models import Goods
from goods.serializers import GoodsSerializer
from rest_framework import generics, mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets


class GoodsPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 100


class GoodsListView(generics.ListAPIView):
    """
    List all snippets, or create a new snippet.
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination  # 使用自定义的class对列表分页


class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination  # 使用自定义的class对列表分页

