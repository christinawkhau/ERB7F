from django.contrib import admin

# Register your models here.
from .models import Listing
from django.forms import NumberInput
from django.db import models

class ListingAdmin(admin.ModelAdmin):
    list_display="id",'title', 'district', 'is_published', 'rooms','doctor' #tuple no need {}
    list_display_links='id', 'title'        
    list_filter="doctor", #must need comma to indicate tuple, if more than one like line 6, 
                        #no need comma at the end
                        #can show ("is_published",) however even more confusing
    list_editable="is_published", "rooms", #the editable value too small, if want bigger,
    #add line 20
    search_fields="title", "district", "doctor"
    list_per_page=25
    ordering=['-id']
    #  prepopulated_fields={"title":('title',)} #better comment    
    formfield_overrides={
        models.IntegerField:{ #here the field is enlarged for values with more digit to be added
            'widget': NumberInput(attrs={'sizen':'10'}) 
        }, 
    }
    
    show_facets=admin.ShowFacets.ALWAYS 

admin.site.register(Listing, ListingAdmin)
