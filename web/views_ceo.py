from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.views import View
from django_request_mapping import request_mapping

from web.models import Seocho, Seochofood, Ceo


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
                context['center'] = 'adminceo/ceopage.html'
                context['obj'] = obj
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
        return render(request, 'common/home.html')

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








