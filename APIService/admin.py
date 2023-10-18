from django.contrib import admin

from APIService.models import Text
# Register your models here.


@admin.register(Text)
class TextAdmin(admin.ModelAdmin):
    list_display = ['url', 'content']
