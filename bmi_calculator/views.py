from django.shortcuts import render
from django.http import HttpResponse
from test1.models import demo


def calculator(request):
    c=0
    data={}    
    try:
        if request.method=='POST':
            v1=float(request.POST.get('height'))
            v2=float(request.POST.get('weight'))
            c=v2/((v1/100)**2)
            data={
                'out':round(c,2)
            }
            return render(request,"calculator.html",data)
    except:
        pass
    return render(request,"calculator.html",data)
