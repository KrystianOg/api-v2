from django.db import IntegrityError
from django.db.models import F
from rest_framework import status, serializers
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.decorators import action

from .models import Survey, Section, Item
from .serializers import SurveySerializer, SectionSerializer, SurveyInfoSerializer
from .viewsets import IdModelViewSet


class SurveyViewSet(RetrieveModelMixin, GenericViewSet):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        # context['survey_id'] = self.kwargs['survey_id']
        return context

    def retrieve_brief(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = SurveyInfoSerializer(instance)
        return Response(serializer.data)


class SectionViewSet(IdModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
