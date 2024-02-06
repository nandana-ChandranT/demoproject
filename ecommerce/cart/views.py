from django.shortcuts import render
from shop.models import Product
from cart.models import Cart
# Create your views here.
def cartview(request):
    u=request.user
    cart=Cart.objects.filter(user=u)
    total=0
    for i in cart:
        total+=i.quantity*i.product.price

    return render(request,'cartview.html',{'c':cart,'total':total})
def addtocart(request,n):
    p=Product.objects.get(name=n) #
    u=request.user #current login user
    try:
        cart=Cart.objects.get(user=u,product=p)
        if(cart.quantity<cart.product.stock):
            cart.quantity+=1
            cart.save()
    except:
        if (p.stock>0):
            cart=Cart.objects.create(product=p,user=u,quantity=1)
            cart.save()

    return cartview(request)


def remove(request,n):
    p=Product.objects.get(name=n) #
    u=request.user #current login user
    try:
        cart=Cart.objects.get(user=u,product=p)
        if cart.quantity > 1:
            cart.quantity-=1
            cart.save()
        else:
            cart.delete()
    except cart.Doesnotexist:
        pass
    return cartview(request)


def delete(request,n):
    p=Product.objects.get(name=n) #
    u=request.user #current login user
    try:
        cart=Cart.objects.get(user=u,product=p)
        if cart.quantity:

            cart.delete()
        else:
            cart.delete()
    except:
        pass
    return cartview(request)

# def orderform(request):
#
#  if ac.amount>=total:
#      ac.amount=ac.amount-total
#      ac.save()
#      for i in cart:
#          o=Order.objects.create(user=u,product=i.product,address=a,phone=p,no_of_items=i.quantity,order_status="paid")
#     return render(request,'orderform.html')
