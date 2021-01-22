# from django.shortcuts import render
# from django.http import HttpResponse
from django.views import generic
from .models import Customer,Store, Order, Product
from django.shortcuts import render

# def index(request):
#     return HttpResponse('Hello world')

class Index(generic.TemplateView):
    template_name='index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['num_orders'] = Order.objects.all().count()
        context['num_customers'] = Customer.objects.count()
        return context


def indexvch(request):
    return render(request, 'index.html')

