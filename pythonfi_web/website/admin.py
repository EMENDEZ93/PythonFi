from django.contrib import admin
from pythonfi_web.website.models import ModelTest


class ModelTestAdmin(admin.ModelAdmin):
    list_display = ('nametest',)
    ordering = ('id',)
    list_filter = ('nametest',)
    search_fields = ('nametest',)

admin.site.register(ModelTest, ModelTestAdmin)
