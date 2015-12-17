from django.http import HttpResponse
from django.shortcuts import redirect, render
from lists.models import Item, List
import random


# Create your views here.
def add_item(request, list_id):
   list_ = List.objects.get(id=list_id)
   n = random.randint(1,30)
   text=request.POST['item_text']
   
   x = int(text)

   item = Item()
   item.angka = x
   item.angkaacak = n
   item.statusnya = status(x, n)
   item.list = list_
   item.save()
   return redirect('/lists/%d/' % (list_.id,))

def view_list(request, list_id):
   list_ = List.objects.get(id=list_id)
   return render(request, 'list.html', {'list': list_})

def home_page(request):
   return render(request, 'home.html')

def new_list(request):
   list_ = List.objects.create()
   n = random.randint(1,30)
   text=request.POST['item_text']
   
   x = int(text)

   item = Item()
   item.angka = x
   item.angkaacak = n
   item.statusnya = status(x, n)
   item.list = list_
   item.save()

   return redirect('/lists/%d/' % (list_.id,))

def status(x, y):
   if x < y+2 and x > y-2:
      return 'Kamu menang!'
   else:
       return 'Kamu kalah!'
