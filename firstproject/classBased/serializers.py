from rest_framework import serializers
from classBased.models import StudentInfoModel

class StudentInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentInfoModel
        fields = "__all__"