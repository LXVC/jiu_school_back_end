import sys

reload(sys)
sys.setdefaultencoding('utf8')

from django.shortcuts import render, Http404, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from question import models as question_models
from education import models as education_models


@login_required
def index(request):
    # query = question_models.Charpter.objects.filter(level=0)
    # serializers = CharpterSerializers(query, many=True)
    return render(request, 'question/index.html', {'user': request.user})


@login_required
def select_subject(request, goto):
    return render(request,
                  'question/select_subject.html',
                  {
                      'subjects': question_models.CodeSubject.objects.all(),
                      'goto': goto
                  })


@login_required
def select_charpter(request, subject_id, goto):
    if request.method == 'GET':
        if goto not in ['question', 'assignment']:
            raise Http404
        return render(request,
                      'question/select_charpter.html',
                      {
                          'subject_id': subject_id,
                          'goto': goto,
                          'nodes': question_models.Charpter.objects.filter(subject_id=subject_id),
                      })
    if request.method == 'POST':
        charpter_id = request.POST.get('charpter_id', None)
        if charpter_id:
            if goto == 'question':
                return redirect(add_question, subject_id, charpter_id)
            elif goto == 'assignment':
                return redirect(add_assignment, subject_id, charpter_id)
            else:
                raise Http404
        else:
            return render(request,
                          'question/select_charpter.html',
                          {
                              'subject_id': subject_id,
                              'goto': goto,
                              'nodes': question_models.Charpter.objects.filter(subject_id=subject_id),
                              'next': True
                          })


@login_required
def add_question(request, subject_id, charpter_id):
    data = {
        'charpter': get_object_or_404(question_models.Charpter, pk=subject_id),
        'subject': get_object_or_404(question_models.CodeSubject, pk=charpter_id),
        'content_type': question_models.CodeQuesthionType.objects.all(),
        'answer_type': question_models.CodeContextType.objects.all()
    }
    if request.method == 'GET':
        return render(request, 'question/add_question.html', data)
    elif request.method == 'POST':
        content = request.POST.get('content', '')
        question_type = get_object_or_404(
            question_models.CodeQuesthionType, pk=request.POST.get('question_type', None))
        answer_type = get_object_or_404(
            question_models.CodeContextType, pk=request.POST.get('answer_type', None))
        difficultly = int(request.POST.get('difficultly', 1))
        solve = request.POST.get('solve', u'')
        owner = education_models.UserOrg.objects.filter(
            user=request.user)[0].org
        library = question_models.Library.objects.filter(owner=owner)[0]
        question = question_models.Question(
            charpter=data['charpter'], content=content, type=question_type,
            owner=owner, answer_type=answer_type, difficultly=difficultly,
            solve=solve, created_by=request.user, edit_by=None, library=library)
        question.save()
        return render(request, 'question/add_question.html', data)


@login_required
def add_assignment(request, subject_id, charpter_id):
    subject = get_object_or_404(question_models.CodeSubject, pk=subject_id)
    charpter = get_object_or_404(question_models.Charpter, pk=charpter_id)
    return render(request, 'question/add_assignment.html', {'charpter': charpter, 'subject': subject})
