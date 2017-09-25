from rest_framework import serializers
from goods.models import Goods, GoodsCategory


# class GoodsSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=50, required=True)
#     click_num = serializers.IntegerField(default=0)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = '__all__'  # 序列化所有的字段


class GoodsSerializer(serializers.ModelSerializer):
    category = CategorySerializer()  # 覆盖掉goods原来的category, 获取category所有信息
    class Meta:
        model = Goods
        fields = '__all__'  # 序列化所有的字段

