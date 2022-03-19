import json

from django.core.paginator import Paginator
from django.db.models import Avg, Count
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django_request_mapping import request_mapping

from web.models import Seocho, Review, Reply


@request_mapping('')
class MyView(View):

    @request_mapping('/')
    def home(self, request):
        # rank_list = Review.objects.select_related('seochono').annotate(avg_star=Avg('star')).filter().order_by('-avg_star')[:9]
        rank_list = Seocho.objects.order_by('-seochono')[:9]
        context = {
            'popular': 'home/popular.html',
            'categori': 'home/categori.html',
            'search': 'home/search.html',
            'seochono': rank_list
        }
        return render(request, 'common/home.html', context)

    @request_mapping("/seocho", method="get")
    def all(self, request):
        page = request.GET.get('page', '1')
        market_list = Seocho.objects.order_by('marketno')
        paginator = Paginator(market_list, 9)
        page_obj = paginator.get_page(page)
        context = {
            'center': 'seocho.html',
            'objs': page_obj
        }
        return render(request, 'seocho.html', context)

    @request_mapping("/search", method="post")
    def search(self, request):
        search = request.POST['search']
        context = {
            'objs': search
        }
        return HttpResponse(json.dumps(context), content_type='application/json')
