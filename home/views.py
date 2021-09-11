from django.shortcuts import render
from .models import PopularProduct, Testimonial


def index(request):
    testimonial = Testimonial.objects.all()[:3]
    popular = PopularProduct.objects.all()[:3]

    context = {
        "testimonial": testimonial,
        "popular": popular
    }
    return render(request, "home/index.html", context)
