from account.views import register
from shop.views import create_product, product_list, create_comment

urlpatterns = [
    ('register/', register),

    ('create_product/', create_product),
    ('product_list/', product_list),
    
    ('create_comment/id', create_comment),
]