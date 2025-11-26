from django.test import TestCase
from django.contrib.auth import get_user_model
from library.models import Book, Author, Category
from orders.services import create_purchase_order
from decimal import Decimal

User = get_user_model()

class PurchaseTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='u1', password='pass', role='member')
        self.author = Author.objects.create(name='A')
        self.cat = Category.objects.create(title='C')
        self.book = Book.objects.create(title='B', author=self.author, category=self.cat, isbn='123', quantity=5, price=Decimal('10.00'))

    def test_create_purchase_order_success(self):
        order = create_purchase_order(self.user, self.book.id, 2)
        self.book.refresh_from_db()
        self.assertEqual(order.total_price, Decimal('20.00'))
        self.assertEqual(self.book.quantity, 3)

    def test_create_purchase_order_not_enough(self):
        from django.core.exceptions import ValidationError
        with self.assertRaises(ValidationError):
            create_purchase_order(self.user, self.book.id, 10)
