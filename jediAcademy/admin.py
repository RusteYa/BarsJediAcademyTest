from django.contrib import admin

from jediAcademy.models import Planet, Candidate, Jedi, PadawanTest, Question, Answer

admin.site.register(Planet)
admin.site.register(Candidate)
admin.site.register(Jedi)
admin.site.register(Question)
admin.site.register(Answer)


class AnswerInline(admin.TabularInline):
    fk_name = "test"
    model = Answer
    extra = 0


@admin.register(PadawanTest)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline, ]
