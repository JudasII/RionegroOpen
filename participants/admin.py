from django.contrib import admin
from .models import Competitor    
from django.utils.html import mark_safe
# Register your models here.


class CompetitorAdmin(admin.ModelAdmin):
    #actions_selection_counter = True
    #actions_on_bottom = False
    #actions_on_top = True

    fields = ('nombres', 'apellidos','documento', 'genero','academia', 'cinturon','pais','ciudad','fechaNacimiento', 'edad', 'categoriaEdad', 'categoriaPeso', 'comprobantePago','verificado', 'comprobante', 'telefono','igtag')
    list_display = [
        'nombres',
        'apellidos',
        'genero',
        'academia',
        'cinturon',
        'edad',
        'categoriaEdad',
        'categoriaPeso',
        'telefono',
        'comprobantePago',
        'verificado',
    ]
    list_display_links=[
        'nombres',
        'verificado'
    ]
    list_filter = [
        'categoriaPeso',
        'academia',
        'cinturon',
        'genero',
        'verificado'
    ]

    readonly_fields = ['comprobantePago', "comprobante"]
    def comprobante(self, obj):
        print(obj)
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url = obj.comprobantePago.url,
            width=obj.comprobantePago.width,
            height=obj.comprobantePago.height,
            )
        )

admin.site.register(Competitor,CompetitorAdmin)