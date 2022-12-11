from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import Question, Choice, Voter
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())



class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'



def vote(request, pk):
    question = get_object_or_404(Question, pk=pk)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        voter = request.POST['voter']
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        if (voter != ""):
            voters_list = Voter.objects.filter(voter_name=voter+":"+str(question.id))
            saved_voter = Voter()
            saved_voter.voter_name = voter+":"+str(question.id)
            saved_voter.chosen_choice = selected_choice
            if(voters_list.count() ==0):
                selected_choice.votes += 1
                selected_choice.save()
                saved_voter.save()
        else:
            # for anonymous choices
            selected_choice.votes += 1
            selected_choice.save()

        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('results', args=(question.id,)))

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([q.question_text for q in latest_question_list])
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)


def results(request, pk):
    question = get_object_or_404(Question, pk=pk)
    template = loader.get_template('polls/results.html')
    voters = Voter.objects.all()
    edited_voters = []

    voters_count_filtered_by_choice = []
    for choice in question.choice_set.all():
        count = Voter.objects.filter(chosen_choice=choice).count()
        voters_count_filtered_by_choice.append({"choice_text": choice.choice_text, "count": count })

    for voter in voters:
        votername_arr=voter.voter_name.split(":")
        edited_voters.append({'choice_text':voter.chosen_choice.choice_text, 'voter_name':votername_arr[0]})
    context = {
        'question': question,
        'voters': edited_voters,#voters,
        'voters_count': voters_count_filtered_by_choice
    }
    return render(request, 'polls/results.html', context)

