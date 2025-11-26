from rest_framework import viewsets, status
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from .models import BorrowRequest, PurchaseOrder
from .serializers import BorrowRequestSerializer, PurchaseOrderSerializer
from .services import approve_borrow_request, reject_borrow_request

class BorrowRequestViewSet(viewsets.ModelViewSet):
    queryset = BorrowRequest.objects.select_related('book', 'user').all()
    serializer_class = BorrowRequestSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'member':
            return self.queryset.filter(user=user)
        return self.queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @extend_schema(description="Approve a borrow request (admin/librarian only).")
    @action(detail=True, methods=['post'], url_path='approve')
    def approve(self, request, pk=None):
        br = self.get_object()
        if request.user.role not in ['librarian', 'admin']:
            return Response({'detail': 'Not allowed'}, status=status.HTTP_403_FORBIDDEN)
        try:
            approve_borrow_request(br, request.user)
        except ValidationError as e:
            raise ValidationError({"detail": f"Cannot approve request: it is already {br.status}."})
        serializer = self.get_serializer(br)
        return Response(serializer.data)

    @extend_schema(description="Reject a borrow request (admin/librarian only).")
    @action(detail=True, methods=['post'], url_path='reject')
    def reject(self, request, pk=None):
        br = self.get_object()
        if request.user.role not in ['admin', 'librarian']:
            return Response({'detail': 'Not allowed'}, status=status.HTTP_403_FORBIDDEN)
        reject_borrow_request(br, request.user)
        serializer = self.get_serializer(br)
        return Response(serializer.data)


class PurchaseOrderViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.select_related('book', 'user').all()
    serializer_class = PurchaseOrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'member':
            return self.queryset.filter(user=user)
        return self.queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
