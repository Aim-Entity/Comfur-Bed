from django.urls import path
from . import views

urlpatterns = [
    path("", views.ProductAllListView.as_view(), name="product"),
    path("bed/", views.ProductBedListView.as_view(), name="bed"),
    path("sofa/", views.ProductSofaListView.as_view(), name="sofa"),
    path("table/", views.ProductTableListView.as_view(), name="table"),
    path("item/<str:slug>", views.ProductAllDetailView.as_view(),
         name="product-detail")
]
