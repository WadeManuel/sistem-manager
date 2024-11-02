from django.contrib import admin
from .models import Vendedor,Cliente,Deportivo,Registro_Compra

class DeportivoAdmin(admin.ModelAdmin):
    list_display = ('modelo','marca','precio')
    search_fields = ('marca',)
    
admin.site.register(Deportivo,DeportivoAdmin)    

# Register your models here.
admin.site.register(Vendedor),
admin.site.register(Cliente),
#admin.site.register(Deportivo),
admin.site.register(Registro_Compra),
