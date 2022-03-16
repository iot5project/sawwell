from django.shortcuts import render
from django.views import View
from django_request_mapping import request_mapping

from web.models import Cust, Review, Reply, Ceo, Seocho


@request_mapping('/review')
class ReviewView(View):

    @request_mapping('/reviewlist/<int:pk>/')
    def reviewlist(self, request, pk):
        obj = Cust.objects.all()
        robjs = Review.objects.all()
        reply_list = Reply.objects.filter(seochono=pk)
        review_list = Review.objects.select_related('seochono').filter(seochono=pk)
        market = Seocho.objects.get(seochono=pk)
        context = {
            'objs': obj,
            'market': market,
            'robjs': robjs,
            'rpobjs': reply_list,
            'real_obj': review_list,
            'center': 'review/list.html',
        }
        return render(request, 'common/main.html', context)

    @request_mapping("/reviewimpl/<int:pk>/", method="post")
    def reviewimpl(self, request, pk):
        star = request.POST['star']
        content = request.POST['content']
        id = request.session['sessionid']
        custno = Cust.objects.get(id=id)
        seochono = Seocho.objects.get(seochono=pk)
        print(star, content)
        context = {'center': 'review/list.html'}
        Review(content=content, star=star, seochono=seochono, custno=custno).save()
        print("write ok")
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
