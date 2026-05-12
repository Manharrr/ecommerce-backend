
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()

from products.models import Category, Brand

def clean_and_seed():
    # Clean duplicates or existing categories/brands if needed
    # But as per user request: "Keep only: Men, Women, Exclusive"
    
    print("Cleaning existing categories and brands...")
    Category.objects.all().delete()
    Brand.objects.all().delete()

    # Seed Categories
    categories = ['Men', 'Women', 'Exclusive']
    for cat_name in categories:
        Category.objects.create(name=cat_name)
    
    print(f"Categories seeded: {categories}")

    # Seed Brands
    brands = [
        'Valentino', 
        'Tom Ford', 
        'Cristiano Ronaldo', 
        'Kayan', 
        'Oud Series', 
        'Elite Oud'
    ]
    for brand_name in brands:
        Brand.objects.create(name=brand_name)
    
    print(f"Brands seeded: {brands}")

if __name__ == "__main__":
    clean_and_seed()
