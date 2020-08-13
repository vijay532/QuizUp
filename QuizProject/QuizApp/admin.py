from django.contrib import admin
from .models import Question,Choice
# Register your models here.

admin.site.site_header="QUIZ DB"
admin.site.site_title="QUIZ Area"
admin.site.index_title="welcome to the quiz area"
class ChoiceInline(admin.TabularInline):
    model=Choice
    #extra=3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': ['question_text']
        }),('Date information',{'fields':['pub_date'],'classes':['collapse']}),
    ]
    inlines=[ChoiceInline,]
    
#admin.site.register(Question)
#admin.site.register(Choice)
admin.site.register(Question,QuestionAdmin)
