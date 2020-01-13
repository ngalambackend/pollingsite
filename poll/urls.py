from django.urls import path

from . import views

app_name = 'poll'

urlpatterns = [
    # ex /poll/
    path('', views.index, name='index'),
    # ex /poll/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex /poll/5/results
    path('<int:question_id>/results/', views.results, name='result'),
    # ex /poll/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote')
]