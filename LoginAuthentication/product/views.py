from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.utils import timezone

from .models import Product



def phome(request):
    # return render(request,'product/phome.html')
    products = Product.objects
    return render(request, 'product/phome.html', {'product': products})


@login_required
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.FILES['image'] and request.FILES['icon'] and request.POST['url']:
            product = Product()
            product.title = request.POST['title']
            product.body = request.POST['body']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                product.url = request.POST['url']
            else:
                product.url = 'http://' + request.POST['url']
                product.icon = request.FILES['icon']
                product.image = request.FILES['image']
                product.pub_date = timezone.now()
                product.hunter = request.user
                product.save()
                return redirect('phome')
                return redirect('/product/' + str(product.id))
        else:
            return render(request, 'product/create.html', {'error': 'Please fill all the fields'})
    else:
       return render(request, 'product/create.html')


def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product/detail.html', {'product': product})

# @login_required
# def upvote(request, product_id):
#         if request.method == 'POST':
#             product == get_object_or_404(Product, pk=product_id)
#             product.votes_total += 1
#             product.save()
#             return redirect('/product/' + str(product.id))