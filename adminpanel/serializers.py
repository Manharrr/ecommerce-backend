from rest_framework import serializers
from django.contrib.auth import get_user_model

from products.models import Perfume, Brand, Category
from orders.models import Order, OrderItem

User = get_user_model()


class AdminUserSerializer(serializers.ModelSerializer):
    orders = AdminOrderSerializer(source='order_set', many=True, read_only=True)

    class Meta:
        model = User
        fields = [
            'id', 'name', 'email', 'is_active', 'is_staff', 
            'is_superuser', 'last_login', 'created_at', 'orders'
        ]


class AdminProductSerializer(serializers.ModelSerializer):

    brand_name = serializers.ReadOnlyField(source="brand.name")
    category_name = serializers.ReadOnlyField( source="category.name" )

    class Meta:
        model = Perfume
        fields = "__all__"


class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"


class AdminOrderItemSerializer(serializers.ModelSerializer):
    perfume_name = serializers.ReadOnlyField(source="perfume.name")
    perfume_image = serializers.ImageField(source="perfume.image", read_only=True)
    perfume_brand = serializers.ReadOnlyField(source="perfume.brand.name")

    class Meta:
        model = OrderItem
        fields = [
            'id', 'order', 'perfume', 'perfume_name', 
            'perfume_image', 'perfume_brand', 'quantity', 'price'
        ]


class AdminOrderSerializer(serializers.ModelSerializer):
    user_email = serializers.ReadOnlyField(source="user.email")
    orderId = serializers.ReadOnlyField(source="id")
    orderDate = serializers.ReadOnlyField(source="created_at")
    totalAmount = serializers.ReadOnlyField(source="total_amount")

    items = AdminOrderItemSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Order
        fields = [
            'id', 'orderId', 'user', 'user_email', 'status', 
            'payment_method', 'totalAmount', 'total_amount', 
            'address', 'orderDate', 'created_at', 'is_paid', 'items'
        ]