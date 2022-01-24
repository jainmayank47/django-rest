from rest_framework import serializers
from functionBased.models import TeacherModel

class TeacherInfoSerialzer(serializers.ModelSerializer):
    class Meta:
        model = TeacherModel
        fields = ("id","name","email","salary")

class TeacherFullInfoSerialzer(serializers.ModelSerializer):
    class Meta:
        model = TeacherModel
        fields = "__all__"