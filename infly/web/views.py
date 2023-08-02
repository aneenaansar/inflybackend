from django.shortcuts import render
from web.models import Category,Item

# Create your views here.

def index(request):
    items =Item.objects.all()[0:4]
    categories = Category.objects.all()

    context = {
        'categories' : categories,
        'items' : items,
                }
    return render(request, 'web/index.html', context)
