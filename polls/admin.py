
from django.contrib import admin

from .models import Choice, ModelLog, Question


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text', 'pub_date']
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):  # noqa: F811
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]


@admin.register(ModelLog)
class ModelLog(admin.ModelAdmin):
    pass


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
