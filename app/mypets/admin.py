from django.contrib import admin
from .models import *
# Register your models here.
class PetsAdmin(admin.ModelAdmin):
    pass

class AdoptionAdmin(admin.ModelAdmin):
    pass
admin.site.register(Pets,PetsAdmin)
admin.site.register(Adoption,AdoptionAdmin)