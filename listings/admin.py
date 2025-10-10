from django.contrib import admin

# Register your models here.
from .models import Listing, Subject
from django.forms import NumberInput
from django.db import models
from django import forms
from taggit.forms import TagWidget
from django.contrib.admin.widgets import FilteredSelectMultiple


class ListingAdminForm(forms.ModelForm):
    subjects=forms.ModelMultipleChoiceField(
        queryset=Subject.objects.all(),
        widget=FilteredSelectMultiple(verbose_name='Professionals', is_stacked=False,
attrs={'rows':'5'}), required=False, label='Select Professionals'
                                   )


    class Meta:
        model=Listing  # this form the model is listing
        fields=[       # we have these fields
            'doctor', 'title', 'address', 'district','description',
            'services', 'service', 'room_type', 'screen',
            'professionals', 'professional','rooms',
            'photo_main', 'photo_1', 'photo_2', 'photo_3',
            'photo_4', 'photo_5', 'photo_6', 'is_published',
        ]
        
        widgets={
            'services': TagWidget(), # Use Taggit's widget for tags  # assign tagwidget function to services     
        }

class ListingAdmin(admin.ModelAdmin):
    form = ListingAdminForm #tailor make display, which item to display
    list_display="id",'title', 'district', 'is_published', 'rooms','doctor', 'tag_list' #tuple no need {}
    list_display_links='id', 'title'        
    list_filter=("doctor", "services") #must need comma to indicate tuple, if more than one like line 6, 
    #no need comma at the end
    #can show ("is_published",) however even more confusing
    list_editable="is_published", "rooms" #the editable value too small, if want bigger, # add line 20
    search_fields=("title", "district", "doctor__name", "services_name") 
    list_per_page=25
   # filter_horizontal = ('services',)
    ordering=['-id']
    #  prepopulated_fields={"title":('title',)} #better comment    
    formfield_overrides={
        models.IntegerField:{ #here the field is enlarged for values with more digit to be added
            'widget': NumberInput(attrs={'size':'10'}) 
        }, 
    }
    
    show_facets=admin.ShowFacets.ALWAYS 


def get_queryset(self, request):
    return super().get_queryset(request).prefetch_related('services') 

def display_subjects(self, obj):
    return", ".join([subject.name for subject in obj.subjects.all()])
display_subjects.short_Description="Professionals"



class SubjectAdmin(admin.ModelAdmin):
    list_display='name',
    search_fields=("name",)
    
admin.site.register(Listing, ListingAdmin)
admin.site.register(Subject, SubjectAdmin)