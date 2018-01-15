from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.views.generic import ListView
from datetime import datetime
from django.urls import reverse
from django.contrib import auth
from loginsys.models import *
from Lab5_App.forms import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import sqlite3

from django.contrib.auth.decorators import login_required


def function_view(request):
    return HttpResponse('response from func view')


class ClassBased(View):
    def get(self, request):
        return HttpResponse('response from class based view')


def main_page(request):
    data = {'services': Service.objects.all()}
    paginate_by = 5

    return render(request, 'orders.html', locals())


class OrdersList(ListView):
    form_class = ServiceForm
    model = Service
    template_name = "orders.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Service.objects.all()
        return context

    def post(self, request):
        form = self.form_class(request.POST or None, request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return HttpResponseRedirect(reverse('order_url', args=(instance.pk,)))
        return render(request, self.template_name, {'form': form})


class AllOrders(ListView):
    form_class = UserServiceForm
    model = UserService
    template_name = "allorders.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = UserService.objects.all()
        return context

    def post(self, request):
        form = self.form_class(request.POST or None, request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return HttpResponseRedirect(reverse('order_url', args=(instance.pk,)))
        return render(request, self.template_name, {'form': form})


def order_add(request):
    users = User.objects.all()
    services = Service.objects.all()
    form = UserServiceForm(request.POST or None, request.FILES or None)
    context = {"form": form, "services": services, "users": users}
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(reverse('orderinfo_url', args=(instance.pk, )))
    return render(request, "order.html", context)


def order_info(request, id):
    userservice = UserService.objects.filter(id=id)
    userservice = userservice.first()
    #if request.POST and titleform.is_valid():

    return render(request, 'orderinfo.html', locals())


def service_info(request, id):
    service = Service.objects.filter(id=id)
    service = service.first()
    #if request.POST and titleform.is_valid():
    orders = UserService.objects.filter(service=id)
    return render(request, 'service.html', locals())
