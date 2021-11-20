from django.urls import path, re_path

from . import views


urlpatterns = [
    path('', views.store, name='store'),
    # path('category/<slug:category_slug>/', views.store, name='products_by_category'),
    # re_path(r'detail/(?P<slug>[-\w]+)/', views.detail),
    #  re_path(r'(?P<slug>[-\w]+)/', views.detail),
    re_path(r'v(?P<category_slug>[-\w]+)/', views.store, name='products_by_category'),

    path('category/<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
    path('search/', views.search, name='search'),
    path('submit_review/<int:product_id>/', views.submit_review, name='submit_review'),
]
