# from collections import Counter
# from django.db.models import Max, Min, F, Count, Avg
from rest_framework import serializers

from .models import Survey, Section, Item, Question


class SurveySerializer(serializers.ModelSerializer):
    sections = serializers.SerializerMethodField()
    items = serializers.SerializerMethodField()

    class Meta:
        model = Survey
        fields = '__all__'

    # TODO: resolve possible N+1 problem
    def get_sections(self, instance):
        sections = instance.get_sections_in_order()
        sections_serializer = SectionSerializer(sections, many=True)
        if len(sections_serializer.data) > 0:
            return sections_serializer.data

    def get_items(self, instance):
        items = instance.get_items_in_order()
        items_serializer = ItemSerializer(items, many=True)  # resolve ItemGetReference
        if len(items_serializer.data) > 0:
            return items_serializer.data


class SurveyInfoSerializer(SurveySerializer):
    sections = None
    items = None

    class Meta(SurveySerializer.Meta):
        fields = '__all__'
        exclude = ('items', 'sections')


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
