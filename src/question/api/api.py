# -*- coding:utf-8 -*-
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import CharpterSerializers, AssignmentSerializers, \
    AssignmentPublishSerializers, AssignmentDetailsSerializers
from education import models as education_models
from question import models as question_models
from django.shortcuts import get_list_or_404

Teacher_id = education_models.CodeRole.objects.get(role_name='教师').id
Student_id = education_models.CodeRole.objects.get(role_name='学生').id


class CharpterViewSet(viewsets.ModelViewSet):
    queryset = question_models.Charpter.objects.filter(level=0)
    serializer_class = CharpterSerializers


class AssignmentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = question_models.AssignmentPublish.objects.all()
    serializer_class = AssignmentPublishSerializers

    def list(self, request, *args, **kwargs):
        if request.user.profile.role_id == Student_id:
            user_orgs_relation = education_models.UserOrg.objects.filter(user=request.user)
            queryset = []
            self.get_teacher_can_see_assignments(request)
            for i in user_orgs_relation:
                queryset.extend(question_models.AssignmentPublish.objects.filter(reciver_org=i.org))
            serializer = AssignmentPublishSerializers(queryset, many=True)
            return Response(serializer.data)
        else:
            assignments = self.get_teacher_can_see_assignments(request)
            serializer = AssignmentSerializers(assignments, many=True)
            return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        if request.user.profile.role_id == Student_id:
            assignment_publish_obj = self.get_object()
            queryset = question_models.AssignmentQuestions.objects.filter(
                assignment_id=assignment_publish_obj.assignment.id)
            serializer = AssignmentDetailsSerializers(queryset, many=True)
            for d in serializer.data:
                d['assignment_publish_id'] = kwargs.get('pk', None)
            return Response(serializer.data)
        else:
            assignment_id = kwargs.get('pk', None)
            queryset = get_list_or_404(question_models.AssignmentQuestions, assignment_id=assignment_id)
            serializer = AssignmentDetailsSerializers(queryset, many=True)
            return Response(serializer.data)

    def get_teacher_can_see_assignments(self, request):
        user_org = education_models.UserOrg.objects.get(user=request.user, org__type_id=1)
        assignments = user_org.org.own_assignments.all()
        return assignments
