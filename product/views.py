from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Product
from .filters import ProductFilter

# def fleet(request):
#     context = {

#     }
#     return render(request, "fleet/fleet.html", context)


class ProductAllListView(ListView):
    template_name = "product/product.html"
    queryset = Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ProductFilter(
            self.request.GET, queryset=self.get_queryset())

        return context


class ProductBedListView(ListView):
    template_name = "product/product_bed.html"
    queryset = Product.objects.filter(category="Beds")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ProductFilter(
            self.request.GET, queryset=self.get_queryset())

        return context


class ProductTableListView(ListView):
    template_name = "product/product_table.html"
    queryset = Product.objects.filter(category="Tables")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ProductFilter(
            self.request.GET, queryset=self.get_queryset())

        return context


class ProductSofaListView(ListView):
    template_name = "product/product_sofa.html"
    queryset = Product.objects.filter(category="Sofas")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ProductFilter(
            self.request.GET, queryset=self.get_queryset())

        return context


class ProductAllDetailView(DetailView):
    template_name = "product/product_detail.html"
    queryset = Product.objects.all()
