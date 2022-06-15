from django.contrib import admin

from futbolec.models import Equipo,Jugador,Campeonato,Campeonatodeequipo

admin.site.register(Equipo)

admin.site.register(Campeonato)

class JugadorAdmin(admin.ModelAdmin):
    list_display = ('nombre' , 'posicion_campo','numero_camiseta','sueldo','equipo_fut')
    search_fields = ('nombre',)
admin.site.register(Jugador, JugadorAdmin)

class CampeonatodeequipoAdmin(admin.ModelAdmin):
    list_display = ('anio','equipo_fut','campeonato')
    search_fields = ('equipo_fut__nombre', 'campeonato__nombre_camp')
admin.site.register(Campeonatodeequipo,CampeonatodeequipoAdmin)
