from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from question import models as question_models
from .api.serializers import CharpterSerializers


# Create your views here.
@login_required
def index(request):
    query = question_models.Charpter.objects.filter(level=0)
    serializers = CharpterSerializers(query, many=True)
    return render(request, 'question/index.html', {'data': serializers.data})
