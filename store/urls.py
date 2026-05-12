from django.urls import path
from .views import (
    ProductListCreateView, ProductDetailView, CategoryListView,
    CartListView, CartAddView, CartRemoveView,
    OrderListView, OrderPlaceView,
)

urlpatterns = [
    path("products/", ProductListCreateView.as_view(), name="product-list"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product-detail"),
    path("categories/", CategoryListView.as_view(), name="category-list"),

    # Cart
    path("cart/", CartListView.as_view(), name="cart-list"),
    path("cart/add/", CartAddView.as_view(), name="cart-add"),
    path("cart/remove/<int:pk>/", CartRemoveView.as_view(), name="cart-remove"),

    # Orders
    path("orders/", OrderListView.as_view(), name="order-list"),
    path("orders/place/", OrderPlaceView.as_view(), name="order-place"),
]
