from django.contrib import admin
from .models import Instrument, Instrument_Level, Subscription, Lesson, Image, Lesson_Minutes, Lesson_Style, Subscription_Months, Lessons_Per_Week


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
admin.site.register(Lesson_Minutes)
admin.site.register(Lesson_Style)
admin.site.register(Subscription_Months)
admin.site.register(Lessons_Per_Week)
