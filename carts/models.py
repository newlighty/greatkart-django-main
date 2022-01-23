from django.db import models
from store.models import Product, Variation
from accounts.models import Account
from django_jalali.db import models as jmodels


# Create your models here.

class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True,verbose_name='آیدی-سبد')
    date_added = jmodels.jDateField(auto_now_add=True,verbose_name='تاریخ اضافه شدن')

    def __str__(self):
        return self.cart_id


class CartItem(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True,verbose_name='کاربر')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,verbose_name='محصول')
    variations = models.ManyToManyField(Variation, blank=True,verbose_name='مشخصه')
    cart    = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True,verbose_name='سبد')
    quantity = models.IntegerField(verbose_name='تعداد')
    is_active = models.BooleanField(default=True,verbose_name='فعال')

    def sub_total(self):
        return self.product.price * self.quantity

    def __unicode__(self):
        return self.product
