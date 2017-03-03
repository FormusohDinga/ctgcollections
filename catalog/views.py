from django.http.response import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from django.views.generic import View
from django.shortcuts import (render, get_object_or_404, redirect)

from django.core.urlresolvers import reverse_lazy



# Create your views here.

from .models import (Dvd, Book, Music, Actor)
from .forms import DvdForm, BookForm
from .utils import (ObjectCreateMixin, ObjectUpdateMixin, ObjectDeleteMixin)

class Catalog(View):
    template_name = 'catalog/catalog.html'
    context = {
        'book_list': Book.objects.all(),
        'dvd_list': Dvd.objects.all()
    }
    def get(self, request, parent_template=None):
        return render(request, self.template_name, self.context)

def book_detail(request, slug):
    book = get_object_or_404(
        Book, slug__iexact=slug)
    return render(
        request,
        'catalog/book_detail.html',
        {'book': book})

class BookList(View):
    template_name = 'catalog/book_list.html'
    def get(self, request, parent_template=None):
        return render(request, self.template_name, {'book_list': Book.objects.all()})

class BookCreate(ObjectCreateMixin,View):
    form_class = BookForm
    template_name = 'catalog/book_form.html'

class BookUpdate(ObjectUpdateMixin, View):
    form_class = BookForm
    template_name = 'catalog/book_update.html'
    model = Book

class BookDelete(ObjectDeleteMixin,View):
    model = Book
    success_url = reverse_lazy(
        'book_list')
    template_name = (
        'catalog/book_confirm_delete.html')


def dvd_detail(request, slug):
    dvd = get_object_or_404(
        Dvd, slug__iexact=slug)
    return render(
        request,
        'catalog/dvd_detail.html',
        {'dvd': dvd})

class DvdList(View):
    template_name = 'catalog/dvd_list.html'
    def get(self, request, parent_template=None):
        return render(request, self.template_name, {'dvd_list': Dvd.objects.all()})

class DvdCreate(ObjectCreateMixin,View):
    form_class = DvdForm
    template_name = 'catalog/dvd_form.html'

class DvdUpdate(ObjectUpdateMixin, View):
    form_class = DvdForm
    template_name = 'catalog/dvd_update.html'
    model = Dvd
class DvdDelete(ObjectDeleteMixin,View):
    model = Dvd
    success_url = reverse_lazy(
        'dvd_list')
    template_name = (
        'catalog/dvd_confirm_delete.html')
