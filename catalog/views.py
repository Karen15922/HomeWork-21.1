from django.views import View
from django.shortcuts import render
from django.views.generic import ListView
from catalog.models import Product
from django.views import View
from django.shortcuts import render, get_object_or_404

class ProductsListView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'

class ProductView(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        context = {'product': product}
        return render(request, 'product.html', context)
    
class ContactsView(View):
    template_name = 'contacts.html'

    def post(self, request):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} {phone} {message}')
        return render(request, self.template_name)

    def get(self, request):
        return render(request, self.template_name)


def product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'product.html', context)