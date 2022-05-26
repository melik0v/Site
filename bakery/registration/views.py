from django.shortcuts import render
from .forms import UserForm
from products.models import *
# Create your views here.


def registration(request):
    form = UserForm(request.POST or None)

    if request.method == 'POST' and form.is_valid:
        # data = form.cleaned_data
        new_form = form.save()

    return render(request, 'registration/registration.html', locals())


def home(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True)
    return render(request, 'registration/home.html', locals())
