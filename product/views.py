from typing import Any
from django.shortcuts import render,get_object_or_404,redirect
from django .views.generic import ListView,DetailView
from .models import Product,Category,Order,OrderItem
from django.http import HttpResponse,JsonResponse
from .cart import Cart
from django .views import View
from django .core.exceptions import ValidationError
import uuid

# Create your views here.
# def index(request):
#     return render(request,'product/index.html')



def cart_summary(request):

    cart=Cart(request)

    products=cart.get_products()
    quantity=cart.get_quantity()
    total=cart.get_total_price()
    all_orders=cart.get_all_info()

    

    data={  
        "products":products,
        "quantities":quantity,
        'all_orders':all_orders,
        "total":total
        }
    return render(request,'product/cart_summary.html',context=data)
def cart_add(request):
    cart=Cart(request)
    
    if request.POST.get('action')=='post':
        product_id=int(request.POST.get('product_id'))
        quantity=request.POST.get('product_quantity')
        
        
        product=get_object_or_404(Product,id=product_id)
        cart.add(product=product, quantity=quantity)


        return JsonResponse({"product_id":product_id})
    return HttpResponse("hello")

def cart_update(request):

    cart=Cart(request)

    if request.POST.get('action')=='post':
        product_id=int(request.POST.get('product_id'))
        quantity=request.POST.get('product_quantity')
        product=get_object_or_404(Product,id=product_id)
        cart.product_update(product, quantity)

    return JsonResponse({"status":"salomm"})

def cart_delete(request):
    cart=Cart(request)
    if request.POST.get('action')=='post':
        print(request.POST.get)
        product_id=request.POST.get('product_id')
        cart.delete_product(product_id)
        return JsonResponse({"status":"salom"}) 



class ProductListView(ListView):
    model=Product
    template_name='product/index.html'
    context_object_name = 'products'
    extra_context={
        "categories":Category.objects.all()
    }


class CategoryProductsList(DetailView):
    model=Category
    template_name='product/index.html'


    context_object_name='products'

    def get_context_data(self,  *args ,**kwargs) :

        context=super(CategoryProductsList,self).get_context_data(*args,**kwargs)
        category=context['product']
        context['product']=category.products.all()
        return context

def about(request,id):
    category=Category.objects.all()
    product=get_object_or_404(Product,pk=id)
    data={
        'category':category,
        'product':product
    }
    return render (request,'product/about.html',context=data)



def savatcham(request,id):
    category=Category.objects.all()
    product=get_object_or_404(Product,pk=id)
    data={
        'category':category,
        'product':product
    }
    return render (request,'product/savatcham.html',context=data)



class ProductDetailView(DetailView):
    model=Product
    template_name='product/detail.html'

    context_object_name='product'



def haqida(request):
    return render (request, 'product/haqida.html')  
class OrderView(View):
    def post(self,request):
        cart=Cart(request)

        all_orders=cart.get_all_info()
        total= cart.get_total_price() 

        #malumot omboriga saqlash
        
        order=Order()
        order.order_id=uuid.uuid4()
        order.total_price=total

        order.user_id=request.user.id
        order.save()
        

        try:
            for item_data in all_orders:
                    order_item=OrderItem()
                    order_item.order=order
                    order_item.product_id=item_data['id']
                    order_item.price=item_data['price']
                    order_item.name=item_data['name']
                    order_item.quantitiy=item_data['quantitiy']
                    order_item.save()
        except:
            cart.clear_cart()
            return redirect('product:index')     

               

        



        return redirect('product:index') 
        #telegram botga habar yuborish