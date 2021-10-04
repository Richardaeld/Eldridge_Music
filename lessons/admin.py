from django.contrib import admin
from .models import Instrument, Instrument_Level, Subscription, Lesson, Image


class InstrumentAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )



class LessonAdmin(admin.ModelAdmin):
    list_display = (
        'instrument',
        'instrument_level',
        'sku',
        'name',
    )

admin.site.register(Image)
admin.site.register(Instrument, InstrumentAdmin)
admin.site.register(Subscription)
admin.site.register(Instrument_Level)
admin.site.register(Lesson, LessonAdmin)