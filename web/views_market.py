from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View
from django_request_mapping import request_mapping

from web.models import Seocho, Categori, Seochofood


@request_mapping('/market')
class MarketView(View):

    @request_mapping('/korea', method='get')
    def chicken(self, request):
        page = request.GET.get('page', '1')
        market_name = Categori.objects.get(categoriname='한식')
        print(market_name)
        market_list = Seocho.objects.filter(categori='한식').order_by('seochono')
        paginator = Paginator(market_list, 9)
        page_obj = paginator.get_page(page)
        context = {
            'objs': page_obj,
            'name': market_name,
            'center': 'market/list.html'

        }
        return render(request, 'common/main.html', context)

    @request_mapping('/japan', method='get')
    def japan(self, request):
        market_name = Categori.objects.get(categoriname='일식')
        page = request.GET.get('page', '1')
        market_list = Seocho.objects.filter(categori='일식').order_by('seochono')
        paginator = Paginator(market_list, 9)
        page_obj = paginator.get_page(page)
        context = {
            'objs': page_obj,
            'name': market_name,
            'center': 'market/list.html'
        }
        return render(request, 'common/main.html', context)
    
    @request_mapping('/america', method='get')
    def america(self, request):
        market_name = Categori.objects.get(categoriname='양식')
        page = request.GET.get('page', '1')
        market_list = Seocho.objects.filter(categori='양식').order_by('seochono')
        paginator = Paginator(market_list, 9)
        page_obj = paginator.get_page(page)
        context = {
            'objs': page_obj,
            'name': market_name,
            'center': 'market/list.html'
        }
        return render(request, 'common/main.html', context)
    
    @request_mapping('/buttet', method='get')
    def buttet(self, request):
        market_name = Categori.objects.get(categoriname='뷔페')
        page = request.GET.get('page', '1')
        market_list = Seocho.objects.filter(categori='뷔페').order_by('seochono')
        paginator = Paginator(market_list, 9)
        page_obj = paginator.get_page(page)
        context = {
            'objs': page_obj,
            'name': market_name,
            'center': 'market/list.html'
        }
        return render(request, 'common/main.html', context)
    
    @request_mapping('/snack', method='get')
    def snack(self, request):
        market_name = Categori.objects.get(categoriname='분식')
        page = request.GET.get('page', '1')
        market_list = Seocho.objects.filter(categori='분식').order_by('seochono')
        paginator = Paginator(market_list, 9)
        page_obj = paginator.get_page(page)
        context = {
            'objs': page_obj,
            'name': market_name,
            'center': 'market/list.html'
        }
        return render(request, 'common/main.html', context)

    @request_mapping('/china', method='get')
    def china(self, request):
        market_name = Categori.objects.get(categoriname='중식')
        page = request.GET.get('page', '1')
        market_list = Seocho.objects.filter(categori='중식').order_by('seochono')
        paginator = Paginator(market_list, 9)
        page_obj = paginator.get_page(page)
        context = {
            'objs': page_obj,
            'name': market_name,
            'center': 'market/list.html'
        }
        return render(request, 'common/main.html', context)

    @request_mapping('/buttet', method='get')
    def buttet(self, request):
        market_name = Categori.objects.get(categoriname='뷔페식')
        page = request.GET.get('page', '1')
        market_list = Seocho.objects.filter(categori='뷔페식').order_by('seochono')
        paginator = Paginator(market_list, 9)
        page_obj = paginator.get_page(page)
        context = {
            'objs': page_obj,
            'name': market_name,
            'center': 'market/list.html'
        }
        return render(request, 'common/main.html', context)
    
    @request_mapping('/etc', method='get')
    def etc(self, request):
        market_name = Categori.objects.get(categoriname='기타')
        page = request.GET.get('page', '1')
        market_list = Seocho.objects.filter(categori='기타').order_by('seochono')
        paginator = Paginator(market_list, 9)
        page_obj = paginator.get_page(page)
        context = {
            'objs': page_obj,
            'name': market_name,
            'center': 'market/list.html'
        }
        return render(request, 'common/main.html', context)

    @request_mapping('/menu/<int:pk>/', method='get')
    def menu(self, request, pk):
        menu_list = Seochofood.objects.filter(seochono=pk)
        market_img = Seocho.objects.get(seochono=pk)
        market_name = Categori.objects.get(categoriname='분식')
        context = {
            'center': 'market/menu.html',
            'name': market_name,
            'menu_list': menu_list,
            'market_img': market_img
        }
        return render(request, 'common/main.html', context)
    
    