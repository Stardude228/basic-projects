from abstract.utils import get_obj_or_404
from .models import Category, Product
from .serializers import ProductSerializer, CategorySerializer

def product_list():
    serializer = ProductSerializer()
    products = serializer.serialize_queryset()
    return products

def product_create():
    title = input('Type a title: ')
    price = input('Type a price: ')
    description = input('Type a description: ')
    quantity = input('Type a quantity: ')

    print('Choose a category: ')
    for category in Category.objects:
        print(category.title)
    category_title = input('======================== \n')
    category = get_obj_or_404(Category, 'title', category_title)

    Product(title, price, description, quantity, category)
    return 'Product has been created successfully!'

def product_detail(product_id):
    product = get_obj_or_404(Product, 'id_', int(product_id))
    serializer = ProductSerializer()
    return serializer.serialize_object(product)

def product_delete(product_id):
    product = get_obj_or_404(Product, 'id_', int(product_id))
    Product.objects.remove(product)
    return 'Product has been deleted successfully!'

def product_update(product_id):
    product = get_obj_or_404(Product, 'id_', int(product_id))
    field = input('Type a aspect that you want to change in product: ')
    if field in dir(product):
        print(f'Old value: {getattr(product, field)}')
        value = input(f'{field} = ')
        setattr(product, field, value)
    else:
        raise Exception('There is no such aspect in product!')
    return product_detail(product_id)

def category_create():
    title = input('Type a title of category: ')
    Category(title)
    return 'Category has been created successfully!'