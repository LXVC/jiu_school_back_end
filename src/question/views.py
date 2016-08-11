from django.shortcuts import render, Http404, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from question import models as question_models


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
    print(subject_id, goto)
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
    if request.method == 'GET':
        subject = get_object_or_404(question_models.CodeSubject, pk=subject_id)
        charpter = get_object_or_404(question_models.Charpter, pk=charpter_id)
        return render(request, 'question/add_question.html', {'charpter': charpter, 'subject': subject})
    elif request.method == 'POST':
        print(request.POST.get('work', ''))
        subject = get_object_or_404(question_models.CodeSubject, pk=subject_id)
        charpter = get_object_or_404(question_models.Charpter, pk=charpter_id)
        return render(request, 'question/add_question.html', {'charpter': charpter, 'subject': subject})


@login_required
def add_assignment(request, subject_id, charpter_id):
    subject = get_object_or_404(question_models.CodeSubject, pk=subject_id)
    charpter = get_object_or_404(question_models.Charpter, pk=charpter_id)
    return render(request, 'question/add_assignment.html', {'charpter': charpter, 'subject': subject})
