from rest_framework import serializers
from .models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    name = serializers.ReadOnlyField(source='perfume.name')
    brand = serializers.ReadOnlyField(source='perfume.brand.name')
    image = serializers.SerializerMethodField()

    class Meta:
        model = OrderItem
        fields = ['id', 'name', 'brand', 'image', 'quantity', 'price']

    def get_image(self, obj):
        if obj.perfume.image:
            return obj.perfume.image
        return None


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    orderId = serializers.ReadOnlyField(source='id')
    orderDate = serializers.ReadOnlyField(source='created_at')
    totalAmount = serializers.ReadOnlyField(source='total_amount')

    class Meta:
        model = Order
        fields = [
            'id', 'orderId', 'orderDate', 'totalAmount', 
            'payment_method', 'address', 'total_amount', 
            'status', 'items', 'created_at'
        ]
