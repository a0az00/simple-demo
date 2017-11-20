from datetime import datetime

from django.db import models


class GoodsProfile(models.Model):
    name = models.CharField(max_length=30, null=False, verbose_name='商品名')
    price = models.FloatField(null=False, verbose_name='价格')
    category = models.ForeignKey(
        'Category',
        related_name='goods_profiles',
        verbose_name='类别'
    )
    img = models.ImageField(
        verbose_name='展示图',
        upload_to='goods/goods_profile/images',
        null=True,
        blank=True
    )
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '商品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=10, null=False, verbose_name='商品类别')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '类别'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name