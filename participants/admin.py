from django.contrib import admin
from .models import Competitor       
# Register your models here.


class CompetitorAdmin(admin.ModelAdmin):
    #actions_selection_counter = True
    #actions_on_bottom = False
    #actions_on_top = True

    fields = ('nombres', 'apellidos','documento', 'genero','academia', 'cinturon','pais','ciudad','fechaNacimiento', 'edad', 'categoriaEdad', 'categoriaPeso', 'comprobantePago','verificado')
    list_display = [
        'nombres',
        'apellidos',
        'genero',
        'academia',
        'cinturon',
        'edad',
        'categoriaEdad',
        'categoriaPeso',
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

    
    readonly_fields = ['comprobantePago']
    

admin.site.register(Competitor,CompetitorAdmin)