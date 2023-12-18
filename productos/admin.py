from django.contrib import admin
from .models import Categoria,Producto
# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("id","nombre")

class ProductoAdmin(admin.ModelAdmin):
    exclude = ('creado_en', )#para excluir un producto de la tabla en este caso es la fecha
    list_display = ("nombre","stock","creado_en")

admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Producto,ProductoAdmin)