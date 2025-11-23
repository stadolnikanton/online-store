from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages

from cart.models import Cart, CartItem
from shop.models import Product


class CartView(View):
    def get(self, request):
        if request.user.is_authenticated:
            try:
                cart = Cart.objects.get(user=request.user)
                cart_items = CartItem.objects.filter(cart=cart)
                cart_items_count = cart_items.count()

                subtotal = sum(
                    item.product.price * item.quantity for item in cart_items
                )
                total = subtotal

            except Cart.DoesNotExist:
                cart_items = []
                cart_items_count = 0
        else:
            cart_items = []
            cart_items_count = 0

        context = {
            "cart_items": cart_items,
            "cart_items_count": cart_items_count,
            "subtotal": subtotal,
            "total": total,
        }

        return render(request, "cart/cart.html", context)

    def post(self, request):
        if "remove_item" in request.POST:
            return self.remove_from_cart(request)
        else:
            return self.add_to_cart(request)

    def add_to_cart(self, request):
        user = request.user
        product_id = request.POST.get("product_id")

        if not product_id:
            messages.error(request, "Product not found")
            return redirect(request.META.get("HTTP_REFERER", "/"))

        try:
            product = get_object_or_404(Product, id=product_id)

            cart, created = Cart.objects.get_or_create(user=user)

            cart_item, item_created = CartItem.objects.get_or_create(
                cart=cart, product=product, defaults={"quantity": 1}
            )

            if not item_created:
                cart_item.quantity += 1
                cart_item.save()

            messages.success(request, f"'{product.name}' added to cart")

        except Exception as e:
            messages.error(request, f"Error: {str(e)}")

        return redirect(request.META.get("HTTP_REFERER", "/"))

    def remove_from_cart(self, request):
        user = request.user
        item_id = request.POST.get("item_id")

        if not user.is_authenticated:
            messages.error(request, "Please login")
            return redirect("login")

        try:
            cart_item = CartItem.objects.get(id=item_id, cart__user=user)
            cart_item.delete()
            messages.success(request, "Item removed from cart")
        except CartItem.DoesNotExist:
            messages.error(request, "Item not found")

        return redirect("cart")
