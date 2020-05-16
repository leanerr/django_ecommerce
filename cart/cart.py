from django.conf import settings
from shop.models import Product
from decimal import Decimal

class Cart(object):

    def __init__(self, request):
    #we want to add the data to cart and save it to users_Browser_sessions not in DB
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, product_count=1, update_count=False):
        # we recieve product as a {} 
        # we make product.id our key 
        # product.id is the 'product_id' in the product
        product_id = str(product.id)
        if product_id not in self.cart:
            #if we are adding a new product , that we had not any of this in our cart before
            self.cart[product_id] = {'product_count': 0,
                                     'price': str(product.price)}

        if update_count:
            self.cart[product_id]['product_count'] = product_count
        else:
            #it means we are adding a product to cart that we had not bofore
            self.cart[product_id]['product_count'] += product_count
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, product):
        #product  we get it from DB 
        product_id = str(product)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        #key here probably referes to product.id or the product itself
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product
        # each product that user is adding to cart is an item that has price , product_count , product
        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['product_count']
            yield item

    def __len__(self):
        # it shows that user how many products is added to cart
        # its like item[product_id][product_count +=
        return sum(item['product_count'] for item in self.cart.values())


    def get_total_price(self):
        return sum(Decimal(item['price']) * item['product_count'] for item in self.cart.values())

    def clear(self):
        self.session[settings.CART_SESSION_ID] = {}
        self.session.modified = True
