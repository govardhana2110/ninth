from django.shortcuts import render
from .forms import NameForm
from django.http import HttpResponse
from .models import Name
def get_name(request):
    if request.method=='POST':
        form=NameForm(request.POST)
        if form.is_valid():
            n1=Name(first_name=form.cleaned_data["first_name"],second_name=form.cleaned_data["second_name"])
            return HttpResponse("data saved successfully")
    else:
        form=NameForm()
        return render(request,'name.html',{'form':form})

