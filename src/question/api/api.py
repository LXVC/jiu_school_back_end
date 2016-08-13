from django.utils.timezone import now
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import CharpterSerializers, AssignmentSerializers
from education import models as education_models
from question import models as question_models


class CharpterViewSet(viewsets.ModelViewSet):
    queryset = question_models.Charpter.objects.filter(level=0)
    serializer_class = CharpterSerializers


class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = question_models.AssignmentPublish.objects.all()
    serializer_class = AssignmentSerializers

    def list(self, request, *args, **kwargs):
        user_orgs_relation = education_models.UserOrg.objects.filter(user=request.user)
        queryset = []
        for i in user_orgs_relation:
            queryset.extend(question_models.AssignmentPublish.objects.filter(reciver_org=i.org))
        print(queryset)
        serializer = AssignmentSerializers(queryset, many=True)
        return Response(serializer.data)
