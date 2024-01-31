from django.shortcuts import render
from testapp.models import *
# Create your views here.
def Home_page_View(request):
    return render(request,'testapp/index.html')

def Hyd_View(request):
    my_list=HydJobs.objects.all()
    return render(request,'testapp/hydjobs.html',{'list':my_list})