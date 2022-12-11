from django.urls import path

from . import views

urlpatterns = [
    # ex: / - list all questions
    path('', views.IndexView.as_view(), name='index'),
    # ex: /5/ - show details of the question with id = 5
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /5/results/ - show the vote results
    path('<int:pk>/results/', views.results, name='results'),
    # ex: /5/vote/ - send POST request to update vote count
    path('<int:pk>/vote/', views.vote, name='vote'),
]