from django.db import models
from accounts.models import Account
from store.models import Product, Variation



class Payment(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE,verbose_name='نام')
    payment_id = models.CharField(max_length=100,verbose_name='ایدی پرداخت')
    payment_method = models.CharField(max_length=100,verbose_name='روش پرداخت')
    amount_paid = models.CharField(max_length=100,verbose_name='مقدار پرداخت') # this is the total amount paid
    status = models.CharField(max_length=100,verbose_name='وضعیت')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='ایجاد شده در')

    def __str__(self):
        return self.payment_id

    class Meta:
        verbose_name = 'پرداخت'
        verbose_name_plural = 'پرداخت ها'
        


class Order(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    )

    user = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True,verbose_name='کاربر')
    payment = models.ForeignKey(Payment, on_delete=models.SET_NULL, blank=True, null=True,verbose_name='پرداخت')
    order_number = models.CharField(max_length=20,verbose_name='شماره سفارش')
    first_name = models.CharField(max_length=50,verbose_name='نام')
    last_name = models.CharField(max_length=50,verbose_name='نام خانوادگی')
    phone = models.CharField(max_length=15,verbose_name='تلفن')
    email = models.EmailField(max_length=50,verbose_name='ایمیل')
    address_line_1 = models.CharField(max_length=50,verbose_name='ادرس اول ')
    address_line_2 = models.CharField(max_length=50, blank=True,verbose_name='ادرس دوم')
    country = models.CharField(max_length=50,verbose_name='کشور')
    state = models.CharField(max_length=50,verbose_name='استان')
    city = models.CharField(max_length=50,verbose_name='شهر')
    order_note = models.CharField(max_length=100, blank=True,verbose_name='یاداشت سفارش')
    order_total = models.FloatField() 
    tax = models.FloatField()
    status = models.CharField(max_length=10, choices=STATUS, default='New',verbose_name='وضیت')
    ip = models.CharField(blank=True, max_length=20)
    is_ordered = models.BooleanField(default=False ,verbose_name='سفارش داده شده')
    created_at = models.DateTimeField(auto_now_add=True ,verbose_name='ایجاد شده در')
    updated_at = models.DateTimeField(auto_now=True,verbose_name='بروز شده در')


    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def full_address(self):
        return f'{self.address_line_1} {self.address_line_2}'

    def __str__(self):
        return self.first_name

    
    class Meta:
        verbose_name = 'سفارشات'
        verbose_name_plural = ' سفارش ها'
            


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE,verbose_name='سفارش')
    payment = models.ForeignKey(Payment, on_delete=models.SET_NULL, blank=True, null=True,verbose_name='پرداخت')
    user = models.ForeignKey(Account, on_delete=models.CASCADE,verbose_name='کاربر')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,verbose_name='محصول')
    variations = models.ManyToManyField(Variation, blank=True,verbose_name='مشخصه ها')
    quantity = models.IntegerField()
    product_price = models.FloatField()
    ordered = models.BooleanField(default=False ,verbose_name='سفارش داده شده')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='ایجاد شده')
    updated_at = models.DateTimeField(auto_now=True,verbose_name='بروز شده در')

    def __str__(self):
        return self.product.product_name



    class Meta:
        verbose_name = 'محصولات سفارش'
        verbose_name_plural = 'محصولات سفارش ها'
        