from django.shortcuts import render
from ecom_app.models import Product
from django.db.models import Q
# Create your views here.

def search_results(request):
    products=None;
    query = None;
    if 'q' in request.POST:
        query = request.POST.get('q')
        products = Product.objects.all().filter(Q(name__contains = query) | Q(description__contains = query))
        return render(request,'search.html',{'query':query,'products':products})