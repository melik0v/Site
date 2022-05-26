from django.shortcuts import render
from django.http import HttpResponseNotFound

categories_dict = {
    'instruments': 'instruments.html',
    'about': 'about.html',
}


# Create your views here.
def index(request):
    return render(request, 'index.html', locals())


def show_page(request, page_name):
    link = categories_dict.get(page_name, None)
    if link:
        return render(request, f'main/{link}', locals())
    else:
        return HttpResponseNotFound(f'Такой страницы не существует - {page_name}')
