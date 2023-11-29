from django.shortcuts import render,redirect,get_object_or_404
from staff.models import staffs
from staff.forms import staffForm

def view_staff(request):
    staff= staffs.objects.all()
    return render(request, 'view_staff.html', {'staff':staff})
def add_staff(request):

   if request.method== 'POST':
       form = staffForm(request.POST,request.FILES)
       if form.is_valid():
           form.save()
           return redirect('staff:view_staff')
   else :
     form = staffForm()
     return  render(request, 'add_staff.html', {'form':form})

def update_staff(request, id):
    staff= get_object_or_404(staffs, id=id)

    if request.method == 'POST':
        form = staffForm(request.POST, instance=staff)
        if form.is_valid():
            form.save()
            return redirect('staff:view_staff')  # Redirect to the staff view after editing
    else:
        form = staffForm(instance=staff)

    return render(request, 'update_staff.html', {'form': form, 'staff': staff})
def delete_staff(request, id):
    staff = staffs.objects.get(id=id)
    if request.method == 'POST':
        staff .delete()
        return redirect('staff:view_staff')
    return render(request, 'delete_staff.html', {'staff': staff})