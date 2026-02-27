from django.shortcuts import render, get_object_or_404
from django.views import View
from shop.models import Product
from api.task import get_exchange_rate  # импортируем вашу функцию


class ProductDetail(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)

        exchange_data = get_exchange_rate()

        usd_rate = 1.0
        if exchange_data:
            for currency in exchange_data:
                if currency.get("Cur_Abbreviation") == "USD":
                    usd_rate = currency.get("Cur_OfficialRate", 1.0)
                    break

        price_in_usd = (
            round(float(product.price) // usd_rate, 2) if usd_rate else 0
        )

        context = {
            "product": product,
            "price_in_usd": price_in_usd,
            "usd_rate": usd_rate,
        }
        return render(request, "product/product_detail.html", context)
