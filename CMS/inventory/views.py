from django.shortcuts import render,redirect,get_object_or_404
from .forms import itemForm
from .models import item

def item_list(request):
    items = item.objects.all()
    return render(request, 'item_list.html', {'items': items})

def add_item(request):
    if request.method == 'POST':
        form = itemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory:item_list')
    else:
        form = itemForm()

    return render(request, 'add_item.html', {'form': form})
def update_item(request, id):
    items= get_object_or_404(item, id=id)

    if request.method == 'POST':
        form = itemForm(request.POST, instance=items)
        if form.is_valid():
            form.save()
            return redirect('inventory:item_list')
    else:
        form = itemForm(instance=items)

    return render(request, 'update_item.html', {'form': form,'items':items})
def delete_item(request, id):
    items = get_object_or_404(item, id=id)
    if request.method=='POST':
        item.delete()
        return  redirect('inventory:item_list')
    else:
      return render(request,'delete_item.html',{'items':items})



