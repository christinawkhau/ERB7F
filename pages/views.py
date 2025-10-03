from django.shortcuts import render
from listings.models import Listing

# Create your views here.

# functions

# views.index

def index(request):
#    return HttpResponse("<h1>Hello world!</h1>")
#    print(request.path)
     listings=Listing.objects.filter(is_published=True)[:3]  #[:3]=0,1,2 -- sublist
     context={"listings":listings}
     return render(request, 'pages/index.html', context)
# views.about

def about(request):
#    print(request.path)
    return render(request, 'pages/about.html')