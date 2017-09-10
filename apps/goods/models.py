from datetime import datetime

from django.db import models
from DjangoUeditor.models import UEditorField


class GoodsCategory(models.Model):
    CATEGORY_TYPE = (
        (1, "一级类目"),
        (2, "二级类目"),
        (3, "三级类目"),
    )
    parent_category = models.ForeignKey('self', null=True, blank=True, verbose_name='父目录级别', help_text='父目录')
    name = models.CharField(default='', max_length=30, verbose_name='类别名称')
    code = models.CharField(default='', max_length=30, verbose_name='类别码')
    desc = models.TextField(default='', max_length=200, verbose_name='类别描述', help_text='类别描述')
    category_type = models.CharField(max_length=30, choices=CATEGORY_TYPE, verbose_name='类目级别', help_text='类目级别')
    is_tab = models.BooleanField(default=False, verbose_name='是否导航', help_text='是否导航')
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "商品类别"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class GoodsBrand(models.Model):
    category = models.ForeignKey(GoodsCategory, related_name='brands', null=True, blank=True, verbose_name="商品类目")
    name = models.CharField(default='', max_length=50, verbose_name='品牌名称')
    desc = models.TextField(default='', max_length=500, verbose_name='品牌简介')
    image = models.ImageField(upload_to='brands/', verbose_name='品牌图片')
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "商品品牌"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Goods(models.Model):
    category = models.ForeignKey(GoodsCategory, verbose_name="商品类目")
    name = models.CharField(max_length=50, verbose_name='商品名称')
    goods_sn = models.CharField(max_length=30, default='', verbose_name='商品货号')
    click_num = models.IntegerField(default=0, verbose_name="点击数")
    sold_num = models.IntegerField(default=0, verbose_name="商品销售量")
    fav_num = models.IntegerField(default=0, verbose_name="收藏数")
    goods_num = models.IntegerField(default=0, verbose_name="库存数")
    market_price = models.DecimalField(default=0, max_digits=12, decimal_places=2, verbose_name='市场价格')
    shop_price = models.DecimalField(default=0, max_digits=12, decimal_places=2, verbose_name='商城价格')
    goods_brief = models.TextField(max_length=500, verbose_name='商品简介')
    goods_desc = UEditorField(verbose_name="内容", imagePath="goods/images/", width=1000, height=300,
                              filePath="goods/files/", default='')
    goods_front_image = models.ImageField(upload_to='goods/images/', null=True, blank=True, verbose_name='封面图')
    ship_free = models.BooleanField(default=True, verbose_name='包邮')
    is_new = models.BooleanField(default=False, verbose_name='新品')
    is_hot = models.BooleanField(default=False, verbose_name='热销')
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = '商品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class GoodsImage(models.Model):

    goods = models.ForeignKey(Goods, verbose_name='所属商品', related_name='images')
    image = models.ImageField(upload_to='goods/images/', null=True, blank=True, verbose_name='图片')
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = '商品详情图片'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name


class Banner(models.Model):
    goods = models.ForeignKey(Goods, verbose_name='所属商品')
    image = models.ImageField(upload_to='banner', verbose_name='首页轮播图片')
    index = models.IntegerField(default=0, verbose_name='轮播顺序')
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = '轮播商品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name

