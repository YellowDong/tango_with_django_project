from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # return HttpResponse("Rango says hey there partner! <br/><a href='/rango/about/'>about</a>")
    context = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/index.html', context)


def about(request):
    #return HttpResponse("Rango says here is the about page.<br/><a href='/rango/'>index</a>")
    return render(request, 'rango/about.html')