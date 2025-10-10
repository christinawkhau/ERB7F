from django.shortcuts import render, get_object_or_404
from .models import Listing
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from . choices import district_choices, room_choices, rooms_choices
from django.db.models import Q
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
    
    paginator=Paginator(listings,3) #if 'page'variable comes in , take which segment, 1,2,3 etc, if no take 1 #paginator show how many section in total
    page=request.GET.get('page')
    paged_listings=paginator.get_page(page) #according to 1,2 or 3, take the smaller data set, stick it back to listings #then back to template engine
    context ={"listings":paged_listings} # doing the sorting here #no need change var "listings", only change #data paged_listings #key value pair  or we van put  #context={"listings":listings, "users":Users}
    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    listing=get_object_or_404(Listing, pk=listing_id) #if user press more info while admin stop people accessing, will be breakdown, so need to add an query
    context={"listing":listing}
    return render(request, 'listings/listing.html', context)

def search(request):
    queryset_list=Listing.objects.order_by('-list_date')
    if 'keywords' in request.GET:
        keywords=request.GET['keywords']
        if keywords:
            queryset_list=queryset_list.filter(Q(description__icontains=keywords) | Q(title__icontains=keywords) | Q(doctor__name__icontains=keywords))

    if 'district' in request.GET:
        district =request.GET['district']
        if district:
            queryset_list=queryset_list.filter(district__iexact=district)
    
    if 'rooms' in request.GET:
        rooms =request.GET['rooms']
        if rooms: 
            queryset_list=queryset_list.filter(rooms__lte=rooms)        
    
    if 'room_type' in request.GET:
        room_type =request.GET['room_type']
        if room_type:
            queryset_list = queryset_list.filter(room_type__iexact=room_type)
    paginator=Paginator(queryset_list,3) 
    page=request.GET.get('page')
    paged_listings=paginator.get_page(page) 
   
    context={"listings":paged_listings,
            "district_choices":district_choices,
            "room_choices":room_choices,
            "rooms_choices":rooms_choices,        
            "values":request.GET}    
    return render(request, 'listings/search.html', context)
