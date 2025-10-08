from django.shortcuts import render, get_object_or_404
from .models import Listing
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.

def listings(request):
    listings=Listing.objects.order_by('list_date').filter(is_published=True)
    #can add .filter(is_published=True) after all()istings", onlnly change
    #data paged_listingsy change
    #data paged_listings
    #key value pair  or we van put  
    #select * order by
    #usually optimized resource by organizing the sql
    #query set sequence is not important here as django will optimize how the sql is run to save resource
    
    paginator=Paginator(listings,3) #if 'page'variable comes in , take which segment, 1,2,3 etc, if no take 1
    #paginator show how many section in total
    page=request.GET.get('page')
    paged_listings=paginator.get_page(page) #according to 1,2 or 3, take the smaller data set, stick it back to listings
    #then back to template engine
    context ={"listings":paged_listings} # doing the sorting here 
    #no need change var "listings", only change
    #data paged_listings
    #key value pair  or we van put  
    #context={"listings":listings, "users":Users}
    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    listing=get_object_or_404(Listing, pk=listing_id) #if user press more info while admin stop people accessing, will be breakdown, so need to add an query
    context={"listing":listing}
    return render(request, 'listings/listing.html', context)

def search(request):
    return render(request, 'listings/search.html')
