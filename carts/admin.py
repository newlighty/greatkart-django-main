from django.contrib import admin
from .models import Cart, CartItem
from django_jalali.admin.filters import JDateFieldListFilter
# Register your models here.

class CartAdmin(admin.ModelAdmin):
    list_display = ('cart_id', 'date_added')
    list_filter = (
        ('date_added', JDateFieldListFilter),
    )

class CartItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'cart', 'quantity', 'is_active')

admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)
