from django.shortcuts import render
from .models import Order
from .forms import OrderForm

# Create your views here.
def first_page(request):
    obj_list = Order.objects.all()
    form = OrderForm()
    return render(request, './index.html', {
        'obj_list': obj_list,
        'form': form
    })

def thanks_page(request):
    name = request.POST['name']
    phone = request.POST['phone']
    el = Order(order_name = name, order_phone = phone)
    el.save()
    return render(request, './thanks_page.html', {
        'name': name,
        'phone': phone
    })