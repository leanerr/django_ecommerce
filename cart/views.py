from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

from cart.forms import CartAddProductForm
from .cart import Cart
from shop.models import Product


@require_POST
def cart_add(requset, product_id):
    cart = Cart(requset)
    #base of the product_id that is in the url we find the product from DB
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(requset.POST)
    if form.is_valid():
        cd = form.cleaned_data
        #usinf def add to adding the product that is gotten from DB to cart
        cart.add(product=product,
                 product_count=cd['product_count'],
                 update_count=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    #we are getting the product_id from url
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    #the data that user is writting in form
    #first is adding to cart
    #then from cart is adding to CartAddProductForm and will show there
    cart = Cart(request)
    for item in cart:
        item['update_product_count_form'] = CartAddProductForm(
            initial={'product_count': item['product_count'],
                     'update': True})
    return render(request, 'cart/detail.html', {'cart': cart})
