"""Seed the database with demonstration content.

Every dish, price and review loaded here is SAMPLE DATA for a fictional
restaurant — the brand is a placeholder (see README). Safe to re-run:
rows are matched by slug/name and updated in place.
"""
import os
from datetime import time

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from django.utils.text import slugify

from apps.gallery.models import GalleryImage
from apps.menu.models import MenuCategory, MenuItem
from apps.reservations.models import DiningTable
from apps.restaurants.models import OpeningHours, Restaurant
from apps.reviews.models import Review

CATEGORIES = [
    ("Amuse-Bouche", "Small openings from the kitchen, offered to begin the evening."),
    ("Starters", "First plates — light, precise, seasonal."),
    ("Main Courses", "From the charcoal grill and the stove."),
    ("Seafood", "Day-boat fish and shellfish, prepared simply."),
    ("Signature Dishes", "The plates the house is known for."),
    ("Desserts", "A quiet finish."),
    ("Beverages", "Champagne, cellar wines and house creations."),
]

# name, category, price, description, ingredients, allergens, image, featured
ITEMS = [
    ("Saffron Velouté", "Amuse-Bouche", "14.00",
     "A warm sip of saffron and roasted cauliflower velouté.",
     "Cauliflower, saffron, brown butter, chive oil", "dairy", "", False),
    ("Garden Dumplings", "Amuse-Bouche", "16.00",
     "Steamed garden dumplings with a herb broth.",
     "Leek, herbs, wheat, vegetable broth", "gluten", "/images/dumpling-steamer.jpg", False),
    ("Seared Hokkaido Scallops", "Starters", "32.00",
     "Scallops seared hard, cauliflower velouté, oscietra caviar.",
     "Scallops, cauliflower, caviar, brown butter", "shellfish, dairy",
     "/images/dish-scallops.jpg", True),
    ("Afghan Ashak", "Starters", "24.00",
     "Leek dumplings, spiced yoghurt, split-pea sauce — a house tribute.",
     "Leek, yoghurt, split pea, dried mint, wheat", "gluten, dairy",
     "/images/dish-ashak.jpg", False),
    ("Burrata & Heirloom Tomato", "Starters", "22.00",
     "Creamy burrata, heirloom tomato, aged balsamic, basil oil.",
     "Burrata, tomato, balsamic, basil", "dairy", "", False),
    ("Wagyu Tenderloin", "Main Courses", "68.00",
     "Charcoal-grilled wagyu, smoked aubergine, bone-marrow jus.",
     "Wagyu beef, aubergine, bone marrow, thyme", "",
     "/images/dish-wagyu.jpg", True),
    ("Charcoal Lamb", "Main Courses", "46.00",
     "Lamb grilled over open charcoal, pistachio, pomegranate.",
     "Lamb, pistachio, pomegranate, mint", "nuts", "/images/dish-lamb.jpg", False),
    ("Kabuli Pulao Royale", "Main Courses", "38.00",
     "Slow-cooked lamb over saffron rice, caramelised carrot, raisins.",
     "Lamb, basmati rice, saffron, carrot, raisins, almonds", "nuts",
     "/images/dish-pulao.jpg", False),
    ("Duck à l'Orange", "Main Courses", "44.00",
     "Dry-aged duck, bitter orange, glazed endive.",
     "Duck, orange, endive, honey", "", "", False),
    ("Wild Sea Bass", "Seafood", "52.00",
     "Whole sea bass, fennel, champagne beurre blanc.",
     "Sea bass, fennel, champagne, butter", "fish, dairy",
     "/images/dish-sea.jpg", True),
    ("Oysters, Champagne Mignonette", "Seafood", "28.00",
     "Six oysters with a champagne and shallot mignonette.",
     "Oysters, champagne, shallot, lemon", "shellfish", "", False),
    ("The Élégance Plate", "Signature Dishes", "58.00",
     "The chef's selection of the evening, served at the table.",
     "Seasonal — ask your server", "", "/images/dish-service.jpg", True),
    ("From the Fire", "Signature Dishes", "49.00",
     "A changing cut from the charcoal fire, carved in the room.",
     "Seasonal — ask your server", "", "/images/kitchen-fire.jpg", False),
    ("Caramel Fondant", "Desserts", "18.00",
     "Warm caramel fondant, gold leaf, smoked salt ice cream.",
     "Caramel, chocolate, eggs, dairy", "dairy, eggs",
     "/images/dessert-caramel.jpg", False),
    ("Rose & Pistachio Mille-Feuille", "Desserts", "17.00",
     "Crisp pastry, rose cream, Sicilian pistachio.",
     "Pastry, rose, pistachio, dairy", "gluten, dairy, nuts", "", False),
    ("Signature Saffron Spritz", "Beverages", "19.00",
     "Saffron, citrus and champagne — the house aperitif.",
     "Saffron, citrus, champagne", "", "/images/cocktail-pour.jpg", False),
    ("Champagne, by the Glass", "Beverages", "21.00",
     "A rotating vintage champagne, poured at the table.",
     "Champagne", "", "", False),
    ("Moroccan Mint Tea", "Beverages", "9.00",
     "Fresh mint tea, poured high, served sweet.",
     "Mint, green tea, sugar", "", "", False),
]

TABLES = [
    ("Window One", 2, "Window"), ("Window Two", 2, "Window"),
    ("Salon One", 4, "Salon"), ("Salon Two", 4, "Salon"),
    ("Salon Three", 2, "Salon"), ("Terrace One", 4, "Terrace"),
    ("Terrace Two", 6, "Terrace"), ("The Private Room", 8, "Private"),
]

# weekday (Mon=0), open, close, closed
HOURS = [
    (0, None, None, True),
    (1, time(18, 0), time(22, 30), False),
    (2, time(18, 0), time(22, 30), False),
    (3, time(18, 0), time(22, 30), False),
    (4, time(18, 0), time(23, 30), False),
    (5, time(18, 0), time(23, 30), False),
    (6, time(17, 30), time(22, 0), False),
]

GALLERY = [
    ("/images/dish-service.jpg", "The Arrival", "Course one, served in the salon.", "food"),
    ("/images/hero-interior.jpg", "The Salon", "The main dining room at dusk.", "interior"),
    ("/images/chef-plating.jpg", "At the Pass", "Final touches before the plate leaves.", "kitchen"),
    ("/images/kitchen-fire.jpg", "From the Fire", "The charcoal grill, lit at five.", "kitchen"),
    ("/images/table-setting.jpg", "The Table", "Set for the first seating.", "atmosphere"),
    ("/images/dish-sea.jpg", "From the Sea", "Day-boat fish, champagne beurre blanc.", "food"),
    ("/images/dessert-caramel.jpg", "The Sweet Quiet", "Caramel fondant to finish.", "food"),
    ("/images/cocktail-pour.jpg", "The Bar", "The saffron spritz, poured at the bar.", "atmosphere"),
]

REVIEWS = [
    ("Claire D. (sample)", 5, "Sample review text — an evening of quiet, precise cooking. Replace with genuine guest reviews before launch."),
    ("Omar S. (sample)", 5, "Sample review text — the tasting plate was the highlight of our trip. Replace with genuine guest reviews before launch."),
    ("Elena R. (sample)", 4, "Sample review text — beautiful room, unhurried service. Replace with genuine guest reviews before launch."),
]


class Command(BaseCommand):
    help = "Load demonstration content for Maison Élégance."

    def handle(self, *args, **options):
        restaurant, _ = Restaurant.objects.update_or_create(
            slug="maison-elegance",
            defaults={
                "name": "Maison Élégance",
                "tagline": "Where exceptional cuisine meets timeless elegance.",
                "description": (
                    "A fine-dining room devoted to quiet luxury: charcoal fire, "
                    "seasonal produce and service that never hurries the table. "
                    "Maison Élégance is a demonstration brand — details are "
                    "placeholders until the real house supplies its own."
                ),
                "logo_text": "Maison Élégance",
                "cover_image": "/images/hero-interior.jpg",
                "address": "12 Rue de la Paix, Paris (sample address)",
                "phone": "+33 1 42 00 00 00",
                "email": "reservations@maison-elegance.example",
                "social_links": {"instagram": "#", "facebook": "#", "x": "#"},
            },
        )
        for weekday, open_t, close_t, closed in HOURS:
            OpeningHours.objects.update_or_create(
                restaurant=restaurant, weekday=weekday,
                defaults={"open_time": open_t, "close_time": close_t, "is_closed": closed},
            )

        categories = {}
        for order, (name, description) in enumerate(CATEGORIES, start=1):
            category, _ = MenuCategory.objects.update_or_create(
                slug=slugify(name),
                defaults={"name": name, "description": description,
                          "display_order": order, "is_active": True},
            )
            categories[name] = category

        for order, (name, cat, price, desc, ing, alg, image, featured) in enumerate(ITEMS, start=1):
            MenuItem.objects.update_or_create(
                name=name,
                defaults={
                    "category": categories[cat], "price": price, "description": desc,
                    "ingredients": ing, "allergens": alg, "image": image,
                    "is_featured": featured, "is_available": True, "display_order": order,
                },
            )

        for name, capacity, zone in TABLES:
            DiningTable.objects.update_or_create(
                name=name, defaults={"capacity": capacity, "zone": zone, "is_active": True}
            )

        for order, (image, title, desc, cat) in enumerate(GALLERY, start=1):
            GalleryImage.objects.update_or_create(
                title=title,
                defaults={"image": image, "description": desc, "category": cat,
                          "display_order": order, "is_active": True},
            )

        for name, rating, text in REVIEWS:
            Review.objects.update_or_create(
                customer_name=name, text=text,
                defaults={"rating": rating, "is_approved": True},
            )

        if settings.DEBUG:
            user_model = get_user_model()
            if not user_model.objects.filter(username="manager").exists():
                # Dev-only staff password comes from the environment, never
                # from a hardcoded value: set MAISON_DEV_STAFF_PASSWORD.
                # If it is unset, a random one is generated and printed once.
                password = os.environ.get("MAISON_DEV_STAFF_PASSWORD")
                if not password:
                    password = get_random_string(20)
                    self.stdout.write(
                        "MAISON_DEV_STAFF_PASSWORD is unset — generated a "
                        f"one-off dev password for 'manager': {password}"
                    )
                user_model.objects.create_user(
                    username="manager", password=password,
                    email="manager@maison-elegance.example", is_staff=True,
                )
                self.stdout.write(
                    "Created DEV-ONLY staff user 'manager' "
                    "(only because DEBUG is on — never in production)."
                )

        self.stdout.write(self.style.SUCCESS(
            f"Seeded {Restaurant.objects.count()} restaurant, "
            f"{MenuItem.objects.count()} dishes, {DiningTable.objects.count()} tables, "
            f"{GalleryImage.objects.count()} gallery images, {Review.objects.count()} sample reviews."
        ))
