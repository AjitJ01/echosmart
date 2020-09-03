from product.viewsets import CategoryViewsets
from rest_framework import routers

router = routers.DefaultRouter()
router.register('category',CategoryViewsets)


