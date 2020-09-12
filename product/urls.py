from django.conf.urls import url 
from product.views import ProductView , CategoryView, InventoryView
 
urlpatterns = [ 
    url(r'^api/product$', ProductView.product_list),
    url(r'^api/product/(?P<pk>[0-9]+)$', ProductView.product_detail),

    url(r'^api/category$', CategoryView.category_list),
    url(r'^api/category/(?P<pk>[0-9]+)$', CategoryView.category_detail),
    
    url(r'^api/inventory$', InventoryView.inventory_list),
    url(r'^api/inventory/(?P<pk>[0-9]+)$', InventoryView.inventory_detail),
    
]