from django.contrib import admin
from .models import CarModel,BrandModel,Buy,commnetsModel
admin.site.register(CarModel)
# admin.site.register(BrandModel)
admin.site.register(Buy)
# Register your models here.
class Brand(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
    list_display=['name','slug']
admin.site.register(BrandModel,Brand)
admin.site.register(commnetsModel)

