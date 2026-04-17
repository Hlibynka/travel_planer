from django.contrib import admin, messages
from django.core.exceptions import ValidationError

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

    def delete_model(self, request, obj):
        try:
            obj.delete()
        except ValidationError as e:
            messages.error(request, e.message)

    def delete_queryset(self, request, queryset):
        for obj in queryset:
            if obj.places.filter(is_visited=True).exists():
                messages.error(request, f"Project '{obj.name}' has visited places and cannot be deleted.")
                return
        queryset.delete()

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('external_id', 'project', 'is_visited')
    list_filter = ('is_visited', 'project')