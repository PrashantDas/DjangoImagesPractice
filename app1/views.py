from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product
from django.views.generic import DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.utils import timezone



def make_and_see(request):
    if request.method == 'POST':
        form_instance = ProductForm(request.POST, request.FILES)
        if form_instance.is_valid():
            form_instance.save()
            messages.success(request, 'Picture is saved')
            return redirect('home')
        else:
            messages.error(request, form_instance.errors)
            return redirect('home')
    else:
        context = {'data': Product.objects.all().order_by('?').first(), 'my_form': ProductForm(), 'time': timezone.now}
        return render(request, 'app1/home.html', context)



class DeleteProduct(SuccessMessageMixin, DeleteView):
    model = Product
    success_message = 'Picture was deleted'    
    success_url = reverse_lazy('home')