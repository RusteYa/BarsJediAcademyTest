from django.core.mail import send_mail
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, FormView, TemplateView

from BarsJediAcademyTest import settings
from jediAcademy.forms import CandidateForm, TestForm, JediSelectForm, CandidateSelectForm
from jediAcademy.models import Question, Candidate, Answer, PadawanTest, Jedi


class HomeView(TemplateView):
    template_name = "jediAcademy/home.html"


class AddCandidateView(FormView):
    template_name = 'jediAcademy/candidate_add.html'
    form_class = CandidateForm
    success_url = reverse_lazy("candidate_test")

    def form_valid(self, form):
        candidate = form.save()
        self.request.session['current_candidate_pk'] = candidate.pk
        return super().form_valid(form)


class PadawanTestView(FormView):
    template_name = 'jediAcademy/candidate_test.html'
    success_url = reverse_lazy("home")
    form_class = TestForm

    def form_valid(self, form):
        candidate = Candidate.objects.filter(pk=self.request.session['current_candidate_pk']).first()
        if candidate:
            test, created = PadawanTest.objects.get_or_create(padawan=candidate)
            for q, v in form.cleaned_data.items():
                question = Question.objects.get(pk=q.split('_')[1])
                if question and (v is not None):
                    a = Answer(question=question, answer=v, test=test)
                    a.save()
            return super().form_valid(form)
        else:
            return HttpResponseRedirect(reverse_lazy("candidate_add"))


class SelectJediView(FormView):
    template_name = 'jediAcademy/jedi_select.html'
    form_class = JediSelectForm
    success_url = reverse_lazy("jedi_candidates")

    def form_valid(self, form):
        self.request.session['current_jedi_pk'] = form.cleaned_data['jedi'].pk
        return super().form_valid(form)


class JediCandidatesView(FormView):
    template_name = 'jediAcademy/jedi_candidates.html'
    form_class = CandidateSelectForm

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        planet = Jedi.objects.filter(pk=self.request.session['current_jedi_pk']).first().planet
        form.fields['candidate'].queryset = Candidate.objects.filter(planet=planet, master=None)
        return form

    def form_valid(self, form):
        candidate_id = form.cleaned_data['candidate'].pk
        self.success_url = reverse_lazy("candidate_answers", kwargs={'candidate_id': candidate_id})
        return super().form_valid(form)


class CandidateAnswerView(View):
    template_name = 'jediAcademy/candidate_answers.html'

    def get(self, request, candidate_id):
        answers = Answer.objects.filter(test__padawan__pk=candidate_id)
        return render(request, self.template_name, {'answers': answers})

    def post(self, request, candidate_id):
        answers = Answer.objects.filter(test__padawan__pk=candidate_id)
        padawan = Candidate.objects.filter(pk=candidate_id).first()
        jedi = Jedi.objects.filter(pk=request.session['current_jedi_pk']).first()
        if padawan and jedi:
            limit = 3
            padawans_count = Candidate.objects.filter(master=jedi).count()
            if padawans_count < limit:
                padawan.master = jedi
                padawan.save()
                send_mail('Зачисление в падаваны', 'Вы зачислены в падаваны к {}'.format(jedi),
                          settings.EMAIL_HOST_USER, [padawan.email])
                return render(request, self.template_name,
                              {'answers': answers, 'status': "Зачислен"})
            else:
                return render(request, self.template_name,
                              {'answers': answers, 'status': "Превышено ограничение на число падаванов"})
        else:
            return render(request, self.template_name, {'answers': answers, 'status': "Зачислить не удалось"})


class JediListView(ListView):
    template_name = 'jediAcademy/jedi_list.html'
    model = Jedi
    context_object_name = 'jedi_list'


class JediWithPadawansListView(ListView):
    template_name = 'jediAcademy/jedi_with_padawans_list.html'
    queryset = Jedi.objects.annotate(num_candidates=Count('candidate')).filter(num_candidates__gt=1)
    context_object_name = 'jedi_list'
