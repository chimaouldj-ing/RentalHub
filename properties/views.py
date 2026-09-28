from django.shortcuts import render, get_object_or_404
from .models import Property


def home(request): return render(request, "properties/home.html", {"properties": Property.objects.filter(available=True).order_by("-created_at")})


def property_detail(request, property_id): return render(request, "properties/property_detail.html", {"property": get_object_or_404(Property, id=property_id, available=True)})