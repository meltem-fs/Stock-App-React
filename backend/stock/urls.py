from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import FirmMVS,ProductMVS,BrandMVS,SalesMVS,CategoryMVS,PurchasesMVS

router = DefaultRouter()
router.register("firms",FirmMVS)
router.register("categories",CategoryMVS)
router.register("products",ProductMVS)
router.register("brands",BrandMVS)
router.register("sales",SalesMVS)
router.register("purchases",PurchasesMVS)

urlpatterns = [
    path("",include(router.urls))
]