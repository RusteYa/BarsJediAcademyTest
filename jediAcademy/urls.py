from django.urls import path

from jediAcademy.views import AddCandidateView, PadawanTestView, SelectJediView, JediCandidatesView, \
    CandidateAnswerView, JediListView, JediWithPadawansListView, HomeView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('candidate/add', AddCandidateView.as_view(), name="candidate_add"),
    path('candidate/test', PadawanTestView.as_view(), name="candidate_test"),
    path('jedi/select', SelectJediView.as_view(), name="jedi_select"),
    path('jedi/candidates', JediCandidatesView.as_view(), name="jedi_candidates"),
    path('jedi/candidate/<int:candidate_id>', CandidateAnswerView.as_view(), name="candidate_answers"),
    path('jedi/list', JediListView.as_view(), name="jedi_list"),
    path('jedi/list_with_padawans', JediWithPadawansListView.as_view(), name="jedi_with_padawans_list"),
]
