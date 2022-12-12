from django.shortcuts import render
from .models import Order

# Create your views here.
def first_page(request):
    obj_list = Order.objects.all()
    return render(request, './index.html', {
        'obj_list': obj_list
    })
