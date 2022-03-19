from django.shortcuts import render, redirect
from django.views import View
from django_request_mapping import request_mapping

from web.models import Cust, Review, Reply, Seocho


@request_mapping('/review')
class ReviewView(View):

    @request_mapping('/reviewlist/<int:pk>/')
    def reviewlist(self, request, pk):
        obj = Cust.objects.all()
        robjs = Review.objects.all()
        review_list = Review.objects.select_related('seochono').filter(seochono=pk)
        reply_list = Reply.objects.select_related('ceoid').filter(seochono=pk)
        market = Seocho.objects.get(seochono=pk)
        context = {
            'objs': obj,
            'market': market,
            'robjs': robjs,
            'reply': reply_list,
            'rpobjs': reply_list,
            'real_obj': review_list,
            'center': 'review/list.html',
        }
        return render(request, 'common/main.html', context)

    @request_mapping("/reviewimpl/<int:pk>/", method="post")
    def reviewimpl(self, request, pk):
        star = request.POST['star']
        content = request.POST['content']
        context = dict()
        try:
            id = request.session['sessionid']
            custno = Cust.objects.get(id=id)
            seochono = Seocho.objects.get(seochono=pk)
            print(custno, seochono)
            Review(content=content, star=star, seochono=seochono, custno=custno).save()
            redirect_action = '/review/reviewlist/' + str(pk) + '/'
            return redirect(redirect_action, context)
        except:
            return redirect('/identify/login')

