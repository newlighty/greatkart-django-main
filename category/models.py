from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True,verbose_name='محصول')
    slug=models.SlugField(max_length=100, unique=True, allow_unicode=True) #allow_unicode=True
  
    description = models.TextField(max_length=255, blank=True,verbose_name='توضیحات')
    cat_image = models.ImageField(upload_to='photos/categories', blank=True,verbose_name='تصویر دسته بندی')

    class Meta:
        verbose_name = 'دسته بندی '
        verbose_name_plural = 'دسته بندی ها'

    # def get_absolute_url(self):
    #         return reverse('products_by_category', args=[self.slug])
    
    def get_url(self):
            return reverse('products_by_category', args=[self.slug])
            
    def __str__(self):
        return self.category_name

       
