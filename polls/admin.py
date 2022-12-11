from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Question, Choice


# custom features for admin panel
# TabularInline instead of StackedInline to make it compact

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    # headers in the display of question information table
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    # to enable search in the questions list
    search_fields = ['question_text']

# myModels = [Question, Choice]
admin.site.register(Question,QuestionAdmin)
