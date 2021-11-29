from django.shortcuts import render
from .models import *

# Create your views here.
def watch_list(req):
    obj=watches.objects.all()
    return render(req,'index.html',{'a':obj})