from .models import Product, Comment
from account.models import MyUser
from .serializers import ProductSerializer

def create_product():
    category = input('Type a category: ')
    title = input('Type a title: ')
    price = float(input('Type a price: '))
    description = input('Type a description: \n')
    Product.create(category=category,title=title,price=price,description=description)
    return 'Product has been created successfully!'

def product_list():
    return ProductSerializer().serialize_queryset()

def create_comment(product_id):
    from datetime import datetime
    username = input('Type your username: ')
    user = MyUser.get(username=username)
    product = Product.get_by_id(product_id)
    body = input('Type your comment: \n')
    created_at = datetime.now()
    Comment.create(user=user,product=product,body=body,created_at=created_at,)
    return 'Comment has been created successfully!'