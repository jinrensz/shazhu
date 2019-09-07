from django.conf.urls import url
from szren import views

urlpatterns = [
    url(r'pro/list/', views.ProfessionalListViews.as_view()),
    url(r'sub/list/', views.SubjectsListViews.as_view()),
    url(r'add/choice/', views.AddChoiceViews.as_view())
]
