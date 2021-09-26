from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from myapp.models import *


def show_about_page(request):
    print("about page request")
    name = 'Victor Askvart'
    link = 'https://www.youtube.com'

    data = {
        'name': name,
        'link': link
    }

    return render(request, "about.html", data)


def show_home_page(request):
    cats = Category.objects.all()
    images = Image.objects.all()

    data = {'images': images, 'cats': cats}

    return render(request, "home.html", data)

def show_images_detail(request, iid):
    '''print(cid)
    images = Image.objects.filter(pk=cid)
    data = {'images': images}
    return render(request, "detail.html", data)
'''

    image = get_object_or_404(Image, pk=iid)
    data = {'image': image}
    return render(request, 'detail.html', data)


def show_category_page(request, cid):
    print(cid)
    cats = Category.objects.all()

    category = Category.objects.get(pk=cid)

    images = Image.objects.filter(cat=category)
    data = {'images': images, 'cats': cats}

    return render(request, "home.html", data)




def home(request):
    return redirect('/home')