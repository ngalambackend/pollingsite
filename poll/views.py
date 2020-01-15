from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import Http404

from .models import Question

# writing django apps part 4
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Choice
# generic view
from django.views import generic

# timezone
from django.utils import timezone

# from django.template import loader

# Create your views here.
# def index(request):
#     # return HttpResponse("Welcome to my site")

#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     # template = loader.get_template('poll/index.html')
#     context = {
#         'latest_question_list' : latest_question_list
#     }
#     # return HttpResponse(template.render(context,request))
#     return render(request, 'poll/index.html', context)

# generic view
class IndexView(generic.ListView):
    template_name = 'poll/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        # return Question.objects.order_by('-pub_date')[:5]
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

# def detail(request, question_id):
#     # return HttpResponse("You're looking at question %s." % question_id)
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exist!")
#     # return render(request, 'poll/detail.html', {'question': question})

#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'poll/detail.html', {'question': question})

# generic view
class DetailView(generic.DetailView):
    model = Question
    template_name = 'poll/detail.html'

# def results(request, question_id):
#     # response = "You're looking at the result of question %s."
#     # return HttpResponse(response % question_id)

#     # writing django apps part 4
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'poll/result.html', {'question': question})

class ResultView(generic.DetailView):
    model = Question
    template_name = 'poll/result.html'

def vote(request, question_id):
    # return HttpResponse("You're voting on question %s." % question_id)
    
    # writing django apps part 4
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'poll/detail.html', {
            'question': question,
            'error_message' : "You didn't select a choice"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('poll:result', args=(question_id,)))