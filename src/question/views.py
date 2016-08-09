from django.shortcuts import render, Http404, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from question import models as question_models
from .api.serializers import CharpterSerializers


@login_required
def index(request):
    # query = question_models.Charpter.objects.filter(level=0)
    # serializers = CharpterSerializers(query, many=True)
    print(dir(request.GET))
    return render(request, 'question/index.html', {'user': request.user})


@login_required
def select_charpter(request, goto):
    if request.method == 'GET':
        if goto not in ['question', 'assignment']:
            raise Http404
        charpters = question_models.Charpter.objects.all()
        return render(request, 'question/select_charpter.html', {'goto': goto,
                                                                 'charpters': charpters})
    if request.method == 'POST':
        charpter_id = request.POST.get('charpter_id', None)
        if goto == 'question':
            return redirect(add_question, charpter_id)
        elif goto == 'assignment':
            return redirect(add_assignment, charpter_id)
        else:
            raise Http404


@login_required
def add_question(request, charpter_id):
    charpter = get_object_or_404(question_models.Charpter, pk=int(charpter_id))
    return render(request, 'question/add_question.html', {'charpter': charpter})


@login_required
def add_assignment(request, charpter_id):
    charpter = get_object_or_404(question_models.Charpter, pk=int(charpter_id))
    return render(request, 'question/add_assignment.html', {'charpter': charpter})
