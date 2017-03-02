from django.http.response import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from django.views.generic import View
from django.shortcuts import (render, get_object_or_404, redirect)

from django.core.urlresolvers import reverse_lazy



# Create your views here.

from .models import Dvd
from .forms import DvdForm
from .utils import (ObjectCreateMixin, ObjectUpdateMixin, ObjectDeleteMixin)


def homepage(request):
    movies = Dvd.objects.all()
    template = loader.get_template('catalog/catalog.html')
    context = Context({'dvds':movies})
    output = template.render(context)
    return HttpResponse(output)

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
class DvdDelete(View):
    model = Dvd
    success_url = reverse_lazy(
        'catalog_dvd_urls')
    template_name = (
        'catalog/dvd_confirm_delete.html')
    def get(self,request,slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        context = {"dvd": obj}
        return render(request, self.template_name, context )
    def post(self, request, slug):
        obj = get_object_or_404(
            self.model, slug__iexact=slug)
        obj.delete()
        return HttpResponseRedirect(
            self.success_url)
