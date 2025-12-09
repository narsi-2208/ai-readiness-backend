from django.urls import path
from .views import QuestionsView, SubmitAssessmentView

urlpatterns = [
    path("questions/", QuestionsView.as_view(), name="ai-readiness-questions"),
    path("submit/", SubmitAssessmentView.as_view(), name="ai-readiness-submit"),

]
