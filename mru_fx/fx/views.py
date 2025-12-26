from .models import Currency, Rate
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy, reverse


class CurrencyList(ListView):
    model = Currency

class CurrencyDetail(DetailView):
    model = Currency  

class CurrencyCreate(CreateView):
    model = Currency
    fields = '__all__'
    success_url = reverse_lazy('currency_list')

class CurrencyDelete(DeleteView):
    model = Currency
    success_url = reverse_lazy('currency_list')

class CurrencyUpdate(UpdateView):
    model =  Currency
    fields = '__all__'
    success_url = reverse_lazy('currency_list')

class RateList(ListView):
    model = Rate

class RateDetail(DetailView):
    model = Rate

class RateCreate(CreateView):
    model = Rate
    fields = '__all__'
    success_url = reverse_lazy('rate_list')

class RateDelete(DeleteView):
    model = Rate
    success_url = reverse_lazy('rate_list')

class RateUpdate(UpdateView):
    model =  Rate
    fields = '__all__'
    success_url = reverse_lazy('rate_list')
