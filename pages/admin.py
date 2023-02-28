from django.contrib import admin
from .models import Team
from django.utils.html import format_html
# Register your models here.


class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html(
            '<img src="{}" width="40" style="border-radius:10px"/>'.format(object.photo.url)
        )
    thumbnail.short_description = 'Photo'
    list_display=(
        'id',
        'first_name',
        'last_name',
        'thumbnail',
        'designation',
        'created_date',
        
    )
    list_display_links=('first_name','thumbnail',)
    search_fields=('first_name', 'last_name', 'designation')
    list_filter=('first_name','designation')
    
admin.site.register(Team, TeamAdmin)    