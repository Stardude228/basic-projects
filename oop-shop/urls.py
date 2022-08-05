from shop.views import *
from account.views import *

urlpatterns = [
    ('products/', product_list),
    ('product-create/', product_create),
    ('product-detail/id', product_detail),
    ('product-delete/id', product_delete),
    ('product-update/id', product_update),
    ('category-create/', category_create),
]