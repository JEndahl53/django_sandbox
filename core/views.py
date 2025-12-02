from django.shortcuts import render
from django.http import HttpResponse
from .models import Composer
from django.db.models import Q

# Create your views here.
def home(request):
    return render(request, "home.html")

def counter(request):
    value = int(request.GET.get("value", 0))
    value += 1

    html = f"""
        <span hx-get="/counter/?value={value}"
                hx-swap="outerHTML"
                hx-trigger="click"
                class="font-bold">
            {value}
        </span>
    """

    return HttpResponse(html)

# This page will load only the search UI and htmx components.
def search_page(request):
    return render(request, "search_page.html")

def search_composers(request):
    q = request.GET.get("q", "").strip()

    composers = Composer.objects.all()

    if q:
        terms = q.split()

        for term in terms:
            composers = composers.filter(
                Q(first_name__icontains=term) |
                Q(last_name__icontains=term)
            )

        composers = composers.order_by("last_name", "first_name")
    else:
        composers = []

    return render(request, "partials/composer_results.html", {
        "composers": composers,
    })