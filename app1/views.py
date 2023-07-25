from django.shortcuts import render, redirect
from .models import Product
from django.views.generic import CreateView, ListView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.utils import timezone



class SavePicture(SuccessMessageMixin, CreateView):
    model = Product
    fields = '__all__'
    success_message = 'Picture was Saved'    


class HomeView(ListView):
    model = Product


class DeleteProduct(SuccessMessageMixin, DeleteView):
    model = Product
    success_message = 'Picture was deleted'    
    success_url = reverse_lazy('save')