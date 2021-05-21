from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    name = request.GET.get("name") or "world"
    return render(request, "base.html", {"name": name})
    # return HttpResponse(f"Dude, {name}!")

def welcome_view(request):
    return render(request, 'base.html')


