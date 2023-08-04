from django.contrib import admin

# Register your models here.
from events.models import event,Locations

class eventsAdmin(admin.ModelAdmin):
    list_display=['id','event_name','data','time','location','image','is_liked']
    list_display_links=['id','event_name']
    list_filter=['user_id','time']
    list_editable=['is_liked']
    search_fields=['event_name']
admin.site.register(event,eventsAdmin)
admin.site.register(Locations)

# Register your models here.