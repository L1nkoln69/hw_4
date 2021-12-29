from math import sqrt

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect  # noqa I101
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .forms import Triangle
from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


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


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def triangle(request):
    if request.method == 'POST':
        form = Triangle(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            if form.cleaned_data['Cathetus_1'] and form.cleaned_data['Cathetus_2'] is float:
                Hypotenuse = sqrt((form.cleaned_data['Cathetus_1']) ** 2 + (form.cleaned_data['Cathetus_2']) ** 2)
            return redirect("polls:triangle")
        else:
            form = Triangle()
    else:
        form = Triangle()
    return render(request, 'triangle.html', {
        'form': form,
    })
