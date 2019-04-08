from django import forms

from jediAcademy.models import Candidate, Question, Jedi


class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        exclude = ('master',)


class TestForm(forms.Form):
    def __init__(self, *args, **kwargs):
        questions = Question.objects.all()
        super().__init__(*args, **kwargs)

        if questions:
            for q in questions:
                self.fields['answer_{}'.format(q.pk)] = forms.BooleanField(label=q, initial=True, required=False)


class JediSelectForm(forms.Form):
    jedi = forms.ModelChoiceField(queryset=Jedi.objects.all(), label='Джедай')


class CandidateSelectForm(forms.Form):
    candidate = forms.ModelChoiceField(queryset=Candidate.objects.all(), label='Кандидат')
