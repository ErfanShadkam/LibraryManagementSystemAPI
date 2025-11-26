from django.contrib import admin
from .models import BorrowRequest, PurchaseOrder

@admin.register(BorrowRequest)
class BorrowRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'status', 'requested_at')
    list_filter = ('status', 'requested_at')

@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'quantity', 'total_price', 'status', 'ordered_at')
    list_filter = ('status', 'ordered_at')
