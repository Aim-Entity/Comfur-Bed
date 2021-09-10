from django.urls import path
from . import views

urlpatterns = [
    path("", views.ProductAllListView.as_view(), name="product"),
    # path("first-class/", views.FleetFirstClassListView.as_view(), name="first-class"),
    # path("executive/", views.FleetExecutiveListView.as_view(), name="executive"),
    # path("business/", views.FleetBusinessListView.as_view(), name="business"),
    # path("item/<str:slug>", views.FleetAllDetailView.as_view(), name="fleet-detail")
]
