from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.views import View
from django_request_mapping import request_mapping

from web.models import Seocho, Seochofood, Ceo, Review, Cust, Reply


@request_mapping('/ceo')
class CeoView(View):

    @request_mapping('/login')
    def login(self, request):
        context = {
            'center': 'adminceo/ceologin.html'
        }
        return render(request, 'common/main.html', context)

    @request_mapping("/loginimpl", method="post")
    def loginimpl(self, request):
        id = request.POST['id']
        password = request.POST['password']
        context = dict()
        try:
            cust = Ceo.objects.get(id=id)
            if cust.password == password:
                request.session['sessionid'] = id
                obj = Ceo.objects.get(id=id)
                context['obj'] = obj
                context['center'] = 'adminceo/ceopage.html'
                return render(request, 'common/main.html', context)
            else:
                raise Exception
        except:
            context['center'] = 'adminceo/ceologin.html'
            context['error'] = 'error'
            return render(request, 'common/main.html', context)

    @request_mapping("/mypage", method="get")
    def mypage(self, request):
        id = request.session['sessionid']
        obj = Ceo.objects.get(id=id)
        context = {
            'center': 'adminceo/ceopage.html',
            'obj': obj
        }
        return render(request, 'common/main.html', context)

    @request_mapping('/ceopage/<int:pk>/', method='get')
    def ceopage(self, request, pk):
        menu_list = Seochofood.objects.filter(seochono=pk)
        market_img = Seocho.objects.get(seochono=pk)
        market_name = Seocho.objects.get(seochono=pk)
        context = {
            'center': 'adminceo/ceoadmin.html',
            'name': market_name,
            'menu_list': menu_list,
            'market_img': market_img
        }
        return render(request, 'common/main.html', context)

    @request_mapping("/delete", method="get")
    def delete(self, request):
        id = request.session['sessionid']
        obj = Ceo.objects.get(id=id)
        obj.delete()
        logout(request)
        return redirect('/')

    @request_mapping("/restaurantdelete/<int:pk>/", method="get")
    def rastaurnatDelete(self, request):
        id = request.session['sessionid']
        obj = Seocho.objects.get(id=id)
        obj.delete()
        logout(request)
        return redirect('/')

    @request_mapping("/updateview", method="get")
    def updateview(self, request):
        id = request.session['sessionid']
        obj = Ceo.objects.get(id=id)
        context = {
            'center': 'adminceo/ceoupdate.html',
            'obj': obj
        }
        return render(request, 'common/main.html', context)

    @request_mapping("/update", method="get")
    def update(self, request):
        password = request.GET['password']
        id = request.GET['id']
        name = request.GET['name']
        obj = Ceo.objects.get(id=id)
        obj.password = password
        obj.name = name
        obj.save()
        return redirect('/ceo/mypage')

    @request_mapping("/ceoidfind")
    def ceoidfind(self, request):
        context = {
            'center': 'adminceo/ceoidFind.html'
        }
        return render(request, 'common/main.html', context)

    @request_mapping("/ceopwdfind")
    def ceopwdfind(self, request):
        context = {
            'center': 'adminceo/ceopwdFind.html'
        }
        return render(request, 'common/main.html', context)

    @request_mapping("/ceoidfindimpl", method="post")
    def ceoidfindimpl(self, request):
        name = request.POST.get('name', False)
        context = dict()
        try:
            ceo = Ceo.objects.get(name=name)
            if ceo.name == name:
                context['center'] = 'adminceo/ceoOK_idfind.html'
                context['Find_id'] = ceo.id
            else:
                raise Exception
        except:
            context['center'] = 'adminceo/ceoidFind.html'
            context['error'] = 'error'
        return render(request, 'common/main.html', context)

    @request_mapping("/ceopwdfindimpl", method="post")
    def ceopwdfindimpl(self, request):
        id = request.POST.get('id', False)
        name = request.POST.get('name', False)
        context = dict()
        try:
            ceo = Ceo.objects.get(id=id)
            if ceo.name == name:
                context['center'] = 'adminceo/ceoOK_pwdfind.html'
                context['Find_pwd'] = ceo.password
            else:
                raise Exception
        except:
            context['center'] = 'adminceo/ceopwdFind.html'
            context['error'] = 'error'
        return render(request, 'common/main.html', context)

    @request_mapping('/ceoadmin/<int:pk>/', method='get')
    def ceoadmin(self, request, pk):
        menu_list = Seochofood.objects.filter(seochono=pk)
        market_img = Seocho.objects.get(seochono=pk)
        market_name = Seocho.objects.get(seochono=pk)
        obj = Cust.objects.all()
        robjs = Review.objects.all()
        review_list = Review.objects.select_related('seochono').filter(seochono=pk)
        reply_list = Reply.objects.select_related('ceoid').filter(seochono=pk)
        market = Seocho.objects.get(seochono=pk)
        context = {
            'center': 'adminceo/ceoadmin.html',
            'name': market_name,
            'menu_list': menu_list,
            'market_img': market_img,
            'market': market,
            'robjs': robjs,
            'rpobjs': reply_list,
            'real_obj': review_list,
            'objs': obj,
        }
        return render(request, 'common/main.html', context)

    @request_mapping('/restaurantupdateview/<int:pk>/', method="get")
    def restaurantupdateview(self, request, pk):
        id = request.session['sessionid']
        menu_list = Seochofood.objects.filter(seochono=pk)
        market_img = Seocho.objects.get(seochono=pk)
        market_name = Seocho.objects.get(seochono=pk)
        market = Seocho.objects.get(seochono=pk)
        context = {
            'center': 'adminceo/restaurantupdate.html',
            'name': market_name,
            'menu_list': menu_list,
            'market_img': market_img,
            'market': market,
        }
        return render(request, 'common/main.html', context)

    @request_mapping("/restaurantupdate", method="get")
    def restaurantupdate(self, request):
        name = request.GET['name']
        menu_list = request.GET['menu_list']
        market_img = request.GET['market_img']
        obj = Seocho.objects.get(id=id)
        obj.marketname = name
        obj.save()
        objs = Seochofood.objects.get(foodid=id)
        objs.menu = menu_list
        obj.market_img = market_img
        obj.save()
        return redirect('/ceo/mypage')

    @request_mapping("/replyimpl/<int:pk>/", method="post")
    def replyimpl(self, request, pk):
        pcontent = request.POST['reply']
        reviewno = request.POST['reviewno']
        context = dict()
        try:
            id = request.session['sessionid']
            ceoid = Ceo.objects.get(id=id)
            seochono = Seocho.objects.get(seochono=pk)
            print(ceoid, seochono)
            Reply(pcontent=pcontent, reivewno=reviewno, ceoid=ceoid, seochono=seochono).save()
            redirect_action = 'ceo/ceoadmin/' + str(pk) + '/'
            return redirect(redirect_action, context)
        except:
            context['error'] = 'error'
            redirect_action = '/ceo/ceoadmin/' + str(pk) + '/'
            print(context['error'])
            return redirect(redirect_action, context)









