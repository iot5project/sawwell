from django.shortcuts import render
from django.views import View
from django_request_mapping import request_mapping

from web.models import Cust, Market, Review, Reply, Ceo


@request_mapping('/review')
class ReviewView(View):

    @request_mapping('/reviewlist')
    def reviewlist(self, request):
        obj = Cust.objects.all()
        objects = Market.objects.all()
        robjs = Review.objects.all()
        rpobjs = Review.objects.all()
        realtion = Review.objects.select_related('custno').all()
        print(realtion)
        context = {
            'objs': obj,
            'objects': objects,
            'robjs': robjs,
            'rpobjs': rpobjs,
            'real_obj': realtion,
            'center': 'review/list.html'
        }
        return render(request, 'common/main.html', context)

    @request_mapping("/reviewimpl", method="post")
    def reviewimpl(self, request):
        star = request.POST['star']
        content = request.POST['content']
        market_list = Market.objects.get(marketno='1')
        id = request.session['sessionid']
        custno = Cust.objects.get(id=id)
        print(star, content)
        context = {'center': 'review/list.html'}
        Review(content=content, star=star, marketno=market_list, custno=custno).save()
        print("register ok")
        return render(request, 'common/main.html', context)

    @request_mapping("/replyimpl", method="post")
    def replyimpl(self, request):
        content = request.POST['reply']
        reviewno = Review.objects.get(reviewno='1')
        ceoid = Ceo.objects.get(ceoid='1')
        print(content)
        context = {'center': 'review/list.html'}
        Reply(content=content, reviewno=reviewno, ceoid=ceoid).save()
        print("register ok")
        return render(request, 'common/main.html', context)
