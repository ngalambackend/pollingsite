from django.urls import path

from . import views

app_name = 'poll'

urlpatterns = [
    # ex /poll/
    # path('', views.index, name='index'),
    # generic view
    path('', views.IndexView.as_view(), name='index'),
    # ex /poll/5/
    # path('<int:question_id>/', views.detail, name='detail'),
    # generic view
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex /poll/5/results
    # path('<int:question_id>/result/', views.results, name='result'),
    # generic view
    path('<int:pk>/result/', views.ResultView.as_view(), name='result'),
    # ex /poll/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote')
]