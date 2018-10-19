import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')
import django
django.setup()
from Rango.models import Category, Page


def populate():
    python_pages = [
        {'title': 'Official Python Tutorial',
         'url': 'http://docs.python.org/3/tutorial/', 'views': 128},
        {'title': 'How to Think like a Computer Scientist',
         'url': 'http://www.greenteapress.com/thinkpython', 'views': 64},
        {'title': 'Learn Python in 10 Minutes',
         'url': 'http://www.korokithakis.net/tutorials/python/', 'views': 32}
    ]

    django_pages = [
        {"title": "Official Django Tutorial",
         "url": "https://docs.djangoproject.com/en/1.9/intro/tutorial01/", 'views': 64},
        {"title": "Django Rocks",
         "url": "http://www.djangorocks.com/", 'views': 128},
        {"title": "How to Tango with Django",
         "url": "http://www.tangowithdjango.com/", 'views': 66}
    ]

    other_pages = [
        {"title": "Bottle",
         "url": "http://bottlepy.org/docs/dev/", 'views': 88},
        {"title": "Flask",
         "url": "http://flask.pocoo.org", 'views': 60}
    ]

    cats = {"Python": {"pages": python_pages, "views": 128, "likes": 64},
            "Django": {"pages": django_pages, "views": 64, "likes": 32},
            "Other Frameworks": {"pages": other_pages, "views": 32, "likes": 16},
            "Pascal": {"pages": [], "views": 32, "likes": 16},
            "Perl": {"pages": [], "views": 32, "likes": 16},
            "Php": {"pages": [], "views": 32, "likes": 16},
            "Prolog": {"pages": [], "views": 32, "likes": 16},
            "Programming": {"pages": [], "views": 32, "likes": 16},
            }

    def add_cat(name, views, likes):
        c = Category.objects.get_or_create(name=name)[0]
        c.views = views
        c.likes = likes
        c.save()
        return c

    def add_page(category, title, url, views=0):
        p = Page.objects.get_or_create(category=category, title=title)[0]
        p.url = url
        p.views = views
        p.save()
        return p

    for cat, cat_data in cats.items():
        c = add_cat(cat, cat_data["likes"], cat_data["views"])
        for p in cat_data["pages"]:
            add_page(c, p.get('title', ''), p.get('url', ''), p.get('views', 0))

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(p)))


if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()