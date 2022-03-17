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
                return redirect('/')
            else:
                raise Exception
        except:
            context['center'] = 'adminceo/ceologin.html'
            context['error'] = 'error'
            return render(request, 'common/main.html', context)

    @request_mapping("/idfindimpl", method="post")
    def idfindimpl(self, request):
        email = request.POST.get('email', False)
        context = {}
        try:
            cust = Cust.objects.get(email=email)
            if cust.email == email:
                context['center'] = 'identify/OK_idfind.html'
                context['Find_id'] = cust.id
            else:
                raise Exception
        except:
            context['center'] = 'identify/idfind.html'
            context['error'] = 'error'
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

    @request_mapping("/updateview", method="get")
    def updateview(self, request):
        id = request.session['sessionid']
        obj = Ceo.objects.get(id=id)
        context = {
            'center': 'identify/ceoupdate.html',
            'obj': obj
        }
        return render(request, 'common/main.html', context)

    @request_mapping("/update", method="get")
    def update(self, request):
        password = request.GET['password']
        id = request.GET['id']
        name = request.GET['name']
        email = request.GET['email']
        obj = Ceo.objects.get(id=id)
        obj.name = name
        obj.password = password
        obj.email = email
        obj.save()
        return redirect('/identify/mypage')








