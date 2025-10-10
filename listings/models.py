from django.db import models
from datetime import datetime
from doctors.models import Doctor
from . choices import district_choices, room_choices, rooms_choices
from taggit.managers import TaggableManager

# Create your models here.

class Subject(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Listing(models.Model):
    doctor=models.ForeignKey(Doctor, on_delete=models.DO_NOTHING) #if table clinic is deleted, doctor stay the same, ie do nothing
    title=models.CharField(max_length=200)  #no need declare id, since ORM automaticallly generate ID and no need to define ID
    address=models.CharField(max_length=200)
    district = models.CharField(max_length=50, choices=district_choices.items())
    description=models.TextField(blank=True) #blank=True mean can be no data, optional
    services = TaggableManager(verbose_name="Services")
    service = models.IntegerField()
    room_type = models.CharField(max_length=200, choices=room_choices.items(), default='')
    screen = models.IntegerField()
    professionals = models.ManyToManyField(Subject, blank=True)
    professional = models.IntegerField()
    rooms=models.CharField(max_length=2, choices=rooms_choices.items())
    photo_main=models.ImageField(upload_to='photos/%Y/%x/%d/') #photo use date of upload eg today 29Sep25_001, can even add time
    photo_1=models.ImageField(upload_to='photos/%Y/%x/%d/')
    photo_2=models.ImageField(upload_to='photos/%Y/%x/%d/')
    photo_3=models.ImageField(upload_to='photos/%Y/%x/%d/')
    photo_4=models.ImageField(upload_to='photos/%Y/%x/%d/')
    photo_5=models.ImageField(upload_to='photos/%Y/%x/%d/')
    photo_6=models.ImageField(upload_to='photos/%Y/%x/%d/')
    is_published=models.BooleanField(default=True)  #create a checker for tracking
    list_date=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        #ordering = ('-list_date',)
        indexes = [models.Index(fields=['list_date'])]
# useing this, in database, we force ordering of data, 
#sorting can do multiple fields

    def __str__(self):      #python internal variable
        return self.title
    
    
    def tag_list(self):
        return u", ".join(tag.name for tag in self.services.all()) #list comprehension, u-format here, refer f':
    
    