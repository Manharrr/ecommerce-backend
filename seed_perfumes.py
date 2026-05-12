
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()

from products.models import Category, Brand, Perfume

def seed_perfumes():
    # Ensure categories and brands exist
    men = Category.objects.get(name='Men')
    women = Category.objects.get(name='Women')
    exclusive = Category.objects.get(name='Exclusive')
    
    valentino = Brand.objects.get(name='Valentino')
    tom_ford = Brand.objects.get(name='Tom Ford')
    cr7 = Brand.objects.get(name='Cristiano Ronaldo')

    perfumes = [
        {
            'name': 'Valentino Uomo Born In Roma',
            'brand': valentino,
            'category': men,
            'price': 8500.00,
            'stock': 15,
            'description': 'A woody and spicy fragrance for men.',
            'image': 'https://images.unsplash.com/photo-1541643600914-78b084683601?auto=format&fit=crop&q=80&w=1000'
        },
        {
            'name': 'Tom Ford Black Orchid',
            'brand': tom_ford,
            'category': women,
            'price': 12000.00,
            'stock': 10,
            'description': 'A luxurious and sensual fragrance of rich, dark accords.',
            'image': 'https://images.unsplash.com/photo-1594035910387-fea47794261f?auto=format&fit=crop&q=80&w=1000'
        },
        {
            'name': 'CR7 Game On',
            'brand': cr7,
            'category': exclusive,
            'price': 4500.00,
            'stock': 20,
            'description': 'An addictive fragrance for those who want to master the night.',
            'image': 'https://images.unsplash.com/photo-1592945403244-b3fbafd7f539?auto=format&fit=crop&q=80&w=1000'
        }
    ]

    for p_data in perfumes:
        Perfume.objects.get_or_create(
            name=p_data['name'],
            defaults=p_data
        )
    
    print("Sample perfumes seeded.")

if __name__ == "__main__":
    seed_perfumes()
