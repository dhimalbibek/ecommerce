from pprint import pp
from django.shortcuts import render
from shop.models import product
from shop.forms import createform
from django.http import HttpResponseRedirect
# Create your views here.
def index(request):
    products = product.objects.all()
    return render(request, 'index.html', {'products': products})

def read_view(request,id):
    p =product.objects.get(id=id)
    return render(request,'read.html',{'product':p})

def create_form(request):
        context ={}
    # if request.method =="POST":
        form =createform(data=request.POST or None, files=request.FILES or None)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        context ={
            'form' : form
             }
        return render(request, 'create.html',context)

def update_view(request,id):
    content ={}
    products =product.objects.get(id=id)
    form = createform(request.POST or None,instance=products)
    if form.is_valid():
     form.save()
    content ={
        'form' : form
    }
    return render(request, 'create.html',content)

def delete_view(request,id):
    if request.method =="POST":
        PP =product.objects.get(id=id)
        PP.delete()
        return HttpResponseRedirect('/create')
    return render (request, 'delete.html', {'id':id})





