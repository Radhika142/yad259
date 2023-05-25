from django.shortcuts import render,HttpResponseRedirect
from .forms import studentregistration
from .models import user


# Create your views here.
def add_show(request):
    if request.method == 'POST':
        fm = studentregistration(request.POST)
        if fm.is_valid():
             Name=fm.cleaned_data['Name']
             Email=fm.cleaned_data['Email']
             Password=fm.cleaned_data['Password']
             reg= user(Name=Name,Email=Email,Password=Password)
             reg.save() 
             fm=studentregistration()    
    else: 
        fm=studentregistration()
    stud=user.objects.all()    
    return render(request,'enroll/addandshow.html',{'form':fm,'stu':stud})
def delete_data(request,id):
    if request.method =='POST':
        pi=user.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
def update_data(request,id):
        if request.method == 'POST':
             pi=user.objects.get(pk=id)
             fm = studentregistration(request.POST,instance=pi)
             if fm.is_valid():
                  fm.save()
        else:
              pi=user.objects.get(pk=id)
              fm = studentregistration(instance=pi)
                       
    
        return render(request,'enroll/updatestudent.html',{'form':fm})

             