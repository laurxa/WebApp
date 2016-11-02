from django.contrib import admin

from .models import Citation


class CitationAdmin(admin.ModelAdmin):
    readonly_fields = ('slug', 'created', 'modified',)
    fieldsets = (
        (None, {
            'fields': ('user', 'title', 'content',),
        },),
        ('Additional Information', {
            'fields': ('slug', 'created', 'modified',)
        },)
    )


admin.site.register(Citation, CitationAdmin)
