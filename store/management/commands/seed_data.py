from django.core.management.base import BaseCommand
from store.models import Category, Product


SAMPLE_DATA = [
    {"category": "Electronics", "products": [
        {"name": "Wireless Headphones", "price": "59.99", "description": "Bluetooth over-ear headphones with noise cancellation.", "stock": 50},
        {"name": "Smartphone Stand", "price": "14.99", "description": "Adjustable desk stand for phones and tablets.", "stock": 120},
        {"name": "USB-C Hub", "price": "34.99", "description": "7-in-1 USB-C hub with HDMI, USB 3.0, and SD card reader.", "stock": 75},
    ]},
    {"category": "Clothing", "products": [
        {"name": "Classic White T-Shirt", "price": "19.99", "description": "100% cotton unisex t-shirt.", "stock": 200},
        {"name": "Slim Fit Jeans", "price": "49.99", "description": "Comfortable stretch denim jeans.", "stock": 80},
        {"name": "Hooded Sweatshirt", "price": "39.99", "description": "Warm fleece hoodie available in multiple colors.", "stock": 60},
    ]},
    {"category": "Books", "products": [
        {"name": "Clean Code", "price": "29.99", "description": "A handbook of agile software craftsmanship by Robert C. Martin.", "stock": 40},
        {"name": "The Pragmatic Programmer", "price": "34.99", "description": "Your journey to mastery by David Thomas and Andrew Hunt.", "stock": 35},
        {"name": "Django for Beginners", "price": "24.99", "description": "Build websites with Python and Django.", "stock": 55},
    ]},
    {"category": "Home & Kitchen", "products": [
        {"name": "Stainless Steel Water Bottle", "price": "22.99", "description": "Insulated 32oz bottle, keeps drinks cold 24 hours.", "stock": 150},
        {"name": "Ceramic Coffee Mug", "price": "12.99", "description": "Microwave-safe 12oz mug.", "stock": 100},
        {"name": "Bamboo Cutting Board", "price": "18.99", "description": "Eco-friendly large cutting board with juice groove.", "stock": 90},
    ]},
]


class Command(BaseCommand):
    help = "Seed the database with sample categories and products"

    def handle(self, *args, **kwargs):
        for entry in SAMPLE_DATA:
            category, _ = Category.objects.get_or_create(name=entry["category"])
            for p in entry["products"]:
                Product.objects.get_or_create(
                    name=p["name"],
                    defaults={
                        "price": p["price"],
                        "description": p["description"],
                        "stock": p["stock"],
                        "category": category,
                    },
                )
        self.stdout.write(self.style.SUCCESS("Sample data seeded successfully."))
