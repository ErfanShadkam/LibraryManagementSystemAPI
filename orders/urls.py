from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BorrowRequestViewSet, PurchaseOrderViewSet

router = DefaultRouter()
router.register('borrow-requests', BorrowRequestViewSet)
router.register('purchase-orders', PurchaseOrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
