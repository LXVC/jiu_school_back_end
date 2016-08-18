# -*- coding:utf-8 -*-
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import CharpterSerializers, AssignmentSerializers, \
    AssignmentPublishSerializers, AssignmentDetailsSerializers
from education import models as education_models
from question import models as question_models
from django.shortcuts import get_list_or_404, Http404

Teacher_id = education_models.CodeRole.objects.get(role_name='教师').id
Student_id = education_models.CodeRole.objects.get(role_name='学生').id


class CharpterViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = question_models.Charpter.objects.filter(level=0)
    serializer_class = CharpterSerializers


class AssignmentPublishedViewSet(viewsets.ModelViewSet):
    # 已发布作业接口
    queryset = question_models.AssignmentPublish.objects.all()
    serializer_class = AssignmentPublishSerializers
    details_queryset = question_models.AssignmentQuestions.objects.all()
    details_class = AssignmentDetailsSerializers

    def list(self, request, *args, **kwargs):
        if request.user.profile.role_id == Student_id:
            user_orgs_relation = education_models.UserOrg.objects.filter(user=request.user)
            queryset = []
            for i in user_orgs_relation:
                queryset.extend(self.queryset.filter(reciver_org=i.org))
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data)
        else:
            queryset = self.queryset.filter(publisher=request.user)
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        if request.user.profile.role_id == Student_id:
            assignment_publish_obj = self.get_object()
            queryset = self.details_queryset.filter(assignment_id=assignment_publish_obj.assignment.id)
            serializer = self.details_class(queryset, many=True)
            for d in serializer.data:
                d['assignment_publish_id'] = kwargs.get('pk', None)
            return Response(serializer.data)
        else:
            assignment_id = kwargs.get('pk', None)
            queryset = get_list_or_404(question_models.AssignmentQuestions, assignment_id=assignment_id)
            serializer = AssignmentDetailsSerializers(queryset, many=True)
            return Response(serializer.data)


class AssignmentViewSet(viewsets.ReadOnlyModelViewSet):
    # 全部作业接口
    queryset = question_models.Assignment.objects.all()
    serializer_class = AssignmentSerializers
    details_queryset = question_models.AssignmentQuestions.objects.all()
    details_class = AssignmentDetailsSerializers

    def list(self, request, *args, **kwargs):
        if request.user.profile.role_id == Student_id:
            raise Http404
        else:
            user_org = education_models.UserOrg.objects.get(user=request.user, org__type_id=1)
            queryset = user_org.org.own_assignments.all()
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        if request.user.profile.role_id == Student_id:
            raise Http404
        else:
            assignment_id = kwargs.get('pk', None)
            queryset = get_list_or_404(question_models.AssignmentQuestions, assignment_id=assignment_id)
            serializer = AssignmentDetailsSerializers(queryset, many=True)
            return Response(serializer.data)
