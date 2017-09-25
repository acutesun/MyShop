import json

from django.http import JsonResponse
from django.views.generic import View
from django.core import serializers

from .models import Goods


class GoodsListView(View):
    def get(self, request):
        goods = Goods.objects.all()[:1]
        # from django.forms.models import model_to_dict
        # for good in goods:
        #     json_dict = model_to_dict(good)  # 不能把imagefield序列化
        #     json_list.append(json_dict)

        json_data = serializers.serialize('json', goods)
        json_data = json.loads(json_data)
        return JsonResponse(json_data, safe=False)
