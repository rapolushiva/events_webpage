from django.shortcuts import render
from events.models import event

# Create your views here.
def homepagefun(request):
    return render(request,'homepage.html')



def addevent(request):
    return render(request,'addevent.html')

def showevent(request):
        fetchevent=event.objects.all()
        context={
            'fetchevent':fetchevent
            }
        return render(request, 'showevent.html', context )

#addevent

from events.forms import EventForm
def addevent(request):
    form=EventForm()

    if request.method=="POST":
        form =EventForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    context={
        "formss":form
    }
    return render(request,'addevent.html',context)
def updateevent(request,pk):
    event_update=event.objects.get(id=pk)
    form=EventForm(instance=event_update)
    if request.method=='POST':
        form=foodForm(request.POST,request.FILES, instance=event_update)
        form.save()
        return redirect('showevent')
    context={
        'formss':form
    }

    return render(request,'updateevent.html', context)

def searchbar(request):
    if request.method =='GET':
        query=request.GET.get('query')
        if query:
            event_query=event.objects.filter(event_name__contains=query)                                 #999
            return render(request,'searchbar.html',{'fetchevent':event_query})
        else:
            print("no products in database")
            return render( request,'searchbar.html',{})