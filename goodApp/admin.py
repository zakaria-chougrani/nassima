from django.contrib import admin

from .models import Parent, Enfant


# Register your models here.

class ParentAdmin(admin.ModelAdmin):
    list_display = (
    'id', 'nomComplet', 'cnie', 'etatFamilial', 'tailleMenage', 'habitat', 'adresse', 'tel', 'created_at', 'updated_at')
    search_fields = ('nomComplet', 'cnie')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class EnfantsAdmin(admin.ModelAdmin):
    list_display = ('id', 'genre', 'age', 'etablissement', 'nScol')
    search_fields = ('genre', 'age')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Parent, ParentAdmin)
admin.site.register(Enfant, EnfantsAdmin)
