from django.http import HttpResponse
from django.shortcuts import render
from Rango.models import Category, Page
from Rango.forms import CategoryForm, PageForm


def index(request):
    # return HttpResponse("Rango says hey there partner! <br/><a href='/rango/about/'>about</a>")

    # context = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    # return render(request, 'rango/index.html', context)

    most_like_categories = Category.objects.all().order_by('-likes')[:5]
    most_view_pages = Page.objects.all().order_by('-views')[:5]
    context_dict = {'most_like_categories': most_like_categories, 'most_view_pages': most_view_pages}
    return render(request, 'rango/index.html', context=context_dict)


def show_category(request, category_name_url):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_url)
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


def add_category(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print(form.errors)
    return render(request, 'rango/add_category.html', context={'form': form})


def add_page(request, category_name_url):
    try:
        category = Category.objects.get(slug=category_name_url)
    except Category.DoesNotExist:
        print('no category exit')
        category = None
    form = PageForm()
    if request.method == 'POST':
            form = PageForm(request.POST)
            if form.is_valid():
                if category:
                    page = form.save(commit=False)
                    page.view = 0
                    page.category = category
                    page.save()
                    return show_category(request, category_name_url)
            else:
                print(form.errors)
    context_dict = {'form': form, 'category': category}
    return render(request, 'rango/add_page.html', context_dict)