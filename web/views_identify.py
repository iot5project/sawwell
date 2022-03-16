from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import logout
from django_request_mapping import request_mapping

from web.models import Cust


@request_mapping('/identify')
class IdentifyView(View):

    @request_mapping('/login')
    def login(self, request):
        context = {
            'center': 'identify/logins.html'
        }
        return render(request, 'common/main.html', context)

    @request_mapping("/idfind")
    def idfind(self, request):
        context = {
            'center': 'identify/idFind.html'
        }
        return render(request, 'common/main.html', context)

    @request_mapping("/pwdfind")
    def pwdfind(self, request):
        context = {
            'center': 'identify/pwdFind.html'
        }
        return render(request, 'common/main.html', context)

    @request_mapping('/register')
    def register(self, request):
        context = {
            'center': 'identify/register.html'
        }
        return render(request, 'common/main.html', context)

    @request_mapping('/logout')
    def logout(self, request):
        if request.session['sessionid'] is not None:
            del request.session['sessionid']
        return render(request, 'common/home.html')

    @request_mapping("/loginimpl", method="post")
    def loginimpl(self, request):
        id = request.POST['id']
        password = request.POST['password']
        context = dict()
        try:
            cust = Cust.objects.get(id=id)
            if cust.password == password:
                request.session['sessionid'] = id
                return redirect('/')
            else:
                raise Exception
        except:
            context['center'] = 'identify/logins.html'
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

    @request_mapping("/pwdfindimpl", method="post")
    def pwdfindimpl(self, request):
        id = request.POST.get('id', False)
        email = request.POST.get('email', False)
        context = {}
        try:
            cust = Cust.objects.get(id=id)
            if cust.email == email:
                context['center'] = 'identify/OK_pwdfind.html'
                context['Find_pwd'] = cust.password
            else:
                raise Exception
        except:
            context['center'] = 'identify/pwdFind.html'
            context['error'] = 'error'
        return render(request, 'common/main.html', context)

    @request_mapping("/registerimpl", method="post")
    def registerimpl(self, request):
        id = request.POST['id']
        password = request.POST['password']
        name = request.POST['name']
        address = request.POST['address']
        email = request.POST['email']
        print(id, password, name, address, email)
        context = {}
        try:
            Cust.objects.get(id=id)
            context['center'] = 'identify/register.html'
            context['error'] = 'error'
            return render(request, 'common/main.html', context)
        except:
            Cust(id=id, password=password, name=name, address=address, email=email).save()
            return redirect('/')

    @request_mapping("/mypage", method="get")
    def mypage(self, request):
        id = request.session['sessionid']
        obj = Cust.objects.get(id=id)
        context = {
            'center': 'identify/mypage.html',
            'obj': obj
        }
        return render(request, 'common/main.html', context)

    @request_mapping("/delete", method="get")
    def delete(self, request):
        id = request.session['sessionid']
        obj = Cust.objects.get(id=id)
        obj.delete()
        logout(request)
        return render(request, 'common/home.html')

    @request_mapping("/updateview", method="get")
    def updateview(self, request):
        id = request.session['sessionid']
        obj = Cust.objects.get(id=id)
        context = {
            'center': 'identify/update.html',
            'obj': obj
        }
        return render(request, 'common/main.html', context)

    @request_mapping("/update", method="get")
    def update(self, request):
        password = request.GET['password']
        id = request.GET['id']
        name = request.GET['name']
        email = request.GET['email']
        obj = Cust.objects.get(id=id)
        obj.name = name
        obj.password = password
        obj.email = email
        obj.save()
        return redirect('/identify/mypage')







