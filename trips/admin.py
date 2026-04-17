from django.contrib import admin
from .models import Project, Place


class PlaceInline(admin.TabularInline):
    model = Place
    extra = 0
    readonly_fields = ('external_id',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'is_completed')
    list_filter = ('is_completed',)
    search_fields = ('name',)
    inlines = [PlaceInline]

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('external_id', 'project', 'is_visited')
    list_filter = ('is_visited', 'project')