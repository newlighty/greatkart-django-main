from django.db import models
from category.models import Category
from django.urls import reverse
from accounts.models import Account
from django.db.models import Avg, Count

# Create your models here.

class Product(models.Model):
    product_name    = models.CharField(max_length=200, unique=True,verbose_name='نام محصول')
    slug            = models.SlugField(max_length=200, unique=True, allow_unicode=True)
    description     = models.TextField(max_length=500, blank=True,verbose_name='توضیحات')
    price           = models.IntegerField()
    images          = models.ImageField(upload_to='photos/products',verbose_name='تصویر')
    stock           = models.IntegerField()
    is_available    = models.BooleanField(default=True,verbose_name='موجود هست')
    category        = models.ForeignKey(Category, on_delete=models.CASCADE,verbose_name='دسته بندی')
    created_date    = models.DateTimeField(auto_now_add=True,verbose_name='ایجاد شده در')
    modified_date   = models.DateTimeField(auto_now=True,verbose_name='اصلاح شده در')

    


    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.product_name


    class Meta:
        verbose_name = 'محصولات'
        verbose_name_plural = ' محصول ها'
                

    # def __unicode__(self):
    #     return u'%s' % self.slug    

    def averageReview(self):
        reviews = ReviewRating.objects.filter(product=self, status=True).aggregate(average=Avg('rating'))
        avg = 0
        if reviews['average'] is not None:
            avg = float(reviews['average'])
        return avg

    def countReview(self):
        reviews = ReviewRating.objects.filter(product=self, status=True).aggregate(count=Count('id'))
        count = 0
        if reviews['count'] is not None:
            count = int(reviews['count'])
        return count

class VariationManager(models.Manager):



    class Meta:
        verbose_name = 'مدیریت مشخصه'
        verbose_name_plural = ' مدیریت مشخصه ها'


    def colors(self):
        return super(VariationManager, self).filter(variation_category='color', is_active=True)

    def sizes(self):
        return super(VariationManager, self).filter(variation_category='size', is_active=True)

variation_category_choice = (
    ('color', 'color'),
    ('size', 'size'),
)


            
            

class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,verbose_name='محصول')
    variation_category = models.CharField(max_length=100, choices=variation_category_choice,verbose_name='دسته بندی مشخصه')
    variation_value     = models.CharField(max_length=100)
    is_active           = models.BooleanField(default=True,verbose_name='فعال است')
    created_date        = models.DateTimeField(auto_now=True,verbose_name='ایجاد شده در')

    objects = VariationManager()


    class Meta:
        verbose_name = 'مشخصه'
        verbose_name_plural = ' مشخصه ها'
                   

    def __str__(self):
        return self.variation_value




class ReviewRating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,verbose_name='محصول')
    user = models.ForeignKey(Account, on_delete=models.CASCADE,verbose_name='کاربر')
    subject = models.CharField(max_length=100, blank=True,verbose_name='عنوان')
    review = models.TextField(max_length=500, blank=True,verbose_name='نظر')
    rating = models.FloatField()
    ip = models.CharField(max_length=20, blank=True)
    status = models.BooleanField(default=True,verbose_name='وضعیت')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='ایجاد شده در')
    updated_at = models.DateTimeField(auto_now=True,verbose_name='بروز شده در')


    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = ' سفارش ها'


    def __str__(self):
        return self.subject


                   
