from rest_framework import serializers
from .models import *


class InsightModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insight
        fields = "__all__"