from django.http import HttpResponse
from django.shortcuts import render
from Rango.models import Category, Page


def index(request):
    # return HttpResponse("Rango says hey there partner! <br/><a href='/rango/about/'>about</a>")

    # context = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    # return render(request, 'rango/index.html', context)

    categories_list = Category.objects.all().order_by('-likes')[:5]
    context_dict = {'categories': categories_list}
    return render(request, 'rango/index.html', context=context_dict)


def show_category(request, category_name_url):
    context_dict = {}
    try:
        category = Category.objects.filter(slug=category_name_url)
        pages = Page.objects.filter(category=category)
        context_dict["pages"] = pages
        context_dict["category"] = category

    except Category.DoesNotExist:
        context_dict["pages"] = None
        context_dict["category"] = None
    return render(request, 'rango/category.html', context=context_dict)


def about(request):
    # return HttpResponse("Rango says here is the about page.<br/><a href='/rango/'>index</a>")
    return render(request, 'rango/about.html')