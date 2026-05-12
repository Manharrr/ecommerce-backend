
import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()

from products.models import Category, Brand

def seed_data():
    # Categories
    categories = ['Men', 'Women', 'Exclusive']
    for cat_name in categories:
        Category.objects.get_or_create(name=cat_name.lower()) # The current model uses lowercase choices
    
    print("Categories seeded.")

    # Brands
    brands = [
        'Valentino', 
        'Tom Ford', 
        'Cristiano Ronaldo', 
        'Kayan', 
        'Oud Series', 
        'Elite Oud'
    ]
    for brand_name in brands:
        Brand.objects.get_or_create(name=brand_name)
    
    print("Brands seeded.")

if __name__ == "__main__":
    seed_data()
