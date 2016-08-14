from django.utils.timezone import now
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import CharpterSerializers, AssignmentSerializers, AssignmentDetailsSerializers
from education import models as education_models
from question import models as question_models
from education.utils import convert_timezone


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
        for j in queryset:
            j.publish_date = convert_timezone(j.publish_date)
        serializer = AssignmentSerializers(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        assignment_publish_obj = self.get_object()
        queryset = question_models.AssignmentQuestions.objects.filter(
            assignment_id=assignment_publish_obj.assignment.id)
        serializer = AssignmentDetailsSerializers(queryset, many=True)
        # serializer.data['assignment_publish_id'] = kwargs.get('pk', 2)
        for d in serializer.data:
            d['assignment_publish_id'] = kwargs.get('pk', None)
        return Response(serializer.data)
