
from django.shortcuts import render, redirect
from django.contrib import messages
 
# import todo form and models
 
from .forms import akashForm
from .models import akash
 
###############################################
 
 
def index(request):
 
    item_list = akash.objects.order_by("-date")
    if request.method == "POST":
        form = akashForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('akash')
    form = akashForm()
 
    page = {
        "forms": form,
        "list": item_list,
        "title": "AKASH LIST",
    }
    return render(request, 'akash.index.html', page)
 
 
### function to remove item, it receive todo item_id as primary key from url ##
def remove(request, item_id):
    item = Akash.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed !!!")
    return redirect('akash')

