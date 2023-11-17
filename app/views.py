from django.shortcuts import render

# Create your views here.
def virat(request):
    data='virat kohli is the first man in cricket history to break the 50 centuries in ODI international'
    D={'virat':data}
    return render(request,'virat.html',context=D)
