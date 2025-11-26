from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from library.views import BookViewSet, AuthorViewSet, CategoryViewSet
from orders.views import BorrowRequestViewSet, PurchaseOrderViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

# Create a router and register all viewsets
router = DefaultRouter()
router.register('books', BookViewSet, basename='book')
router.register('authors', AuthorViewSet, basename='author')
router.register('categories', CategoryViewSet, basename='category')
router.register('borrow-requests', BorrowRequestViewSet, basename='borrowrequest')
router.register('purchase-orders', PurchaseOrderViewSet, basename='purchaseorder')

urlpatterns = [
    # Admin panel
    path('admin/', admin.site.urls),

    # API routes
    path('api/', include(router.urls)),

    # User registration
    path('api/users/', include('users.urls')),

    # JWT authentication
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # DRF Spectacular (OpenAPI / Swagger)
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
