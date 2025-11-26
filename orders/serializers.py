from rest_framework import serializers
from .models import BorrowRequest, PurchaseOrder
from .services import create_purchase_order, create_borrow_request

class BorrowRequestSerializer(serializers.ModelSerializer):
    book_id = serializers.IntegerField(write_only=True, required=True)
    book = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = BorrowRequest
        fields = ('id', 'user', 'book', 'book_id', 'requested_at', 'status')
        read_only_fields = ('user', 'requested_at', 'status')

    def create(self, validated_data):
        user = self.context['request'].user
        book_id = validated_data.pop('book_id')
        return create_borrow_request(user, book_id)


class PurchaseOrderSerializer(serializers.ModelSerializer):
    book_id = serializers.IntegerField(write_only=True, required=True)
    book = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = PurchaseOrder
        fields = ('id', 'user', 'book', 'book_id', 'quantity', 'total_price', 'ordered_at', 'status')
        read_only_fields = ('user', 'total_price', 'ordered_at', 'status')

    def create(self, validated_data):
        user = self.context['request'].user
        book_id = validated_data.pop('book_id')
        quantity = validated_data.get('quantity', 1)
        return create_purchase_order(user, book_id, quantity)
