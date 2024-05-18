from rest_framework import serializers
from .models import report


class ReportPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = report
        fields = ['id','organization', 'centername', 'date', 'subject', 'description', 'oncall']
