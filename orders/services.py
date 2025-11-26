from django.db import transaction
from django.utils import timezone
from decimal import Decimal
from rest_framework.exceptions import ValidationError
from library.models import Book
from .models import PurchaseOrder, BorrowRequest

def create_purchase_order(user, book_id, quantity):
    if quantity <= 0:
        raise ValidationError("Quantity must be greater than 0")

    with transaction.atomic():
        try:
            book = Book.objects.select_for_update().get(id=book_id)
        except Book.DoesNotExist:
            raise ValidationError("Book not found")

        if book.quantity < quantity:
            raise ValidationError("Not enough stock available")

        total_price = (book.price or Decimal('0.00')) * Decimal(quantity)
        book.quantity -= quantity
        book.save()

        order = PurchaseOrder.objects.create(
            user=user,
            book=book,
            quantity=quantity,
            total_price=total_price,
            status='completed',
            ordered_at=timezone.now()
        )
    return order


def create_borrow_request(user, book_id):

    with transaction.atomic():
        try:
            book = Book.objects.select_for_update().get(id=book_id)
        except Book.DoesNotExist:
            raise ValidationError("Book not found")

        br = BorrowRequest.objects.create(
            user=user,
            book=book,
            status='pending'
        )
    return br


def approve_borrow_request(request_obj, approver):
    if request_obj.status != 'pending':
        raise ValidationError({"detail": f"Cannot approve this request, it is already {request_obj.status}."})

    with transaction.atomic():
        book = Book.objects.select_for_update().get(id=request_obj.book.id)
        if book.quantity <= 0:
            raise ValidationError("No copies available to approve the borrow request")

        book.quantity -= 1
        book.save()

        request_obj.status = 'approved'
        request_obj.save()
    return request_obj


def reject_borrow_request(request_obj, approver, reason=None):
    if request_obj.status != 'pending':
        raise ValidationError("Cannot reject a non-pending request")

    request_obj.status = 'rejected'
    # optionally store reason in future
    request_obj.save()
    return request_obj
