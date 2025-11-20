from django.shortcuts import render
from django.http import HttpResponse

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