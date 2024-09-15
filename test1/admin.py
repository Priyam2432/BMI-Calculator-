from django.contrib import admin
from test1.models import demo

# Register your models here
class disp(admin.ModelAdmin):
    list_display=['v']

admin.site.register(demo,disp)



