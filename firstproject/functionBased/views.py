from django.shortcuts import render
from functionBased.models import TeacherModel
from rest_framework.decorators import api_view
from rest_framework.response import Response
from functionBased.serializers import TeacherInfoSerialzer, TeacherFullInfoSerialzer
from rest_framework import status


# Create your views here.
@api_view(["GET","POST"])
def TeacherInfoViews(request):
    if request.method == "GET":
        teacher_list = TeacherModel.objects.all()
        teachers = TeacherInfoSerialzer(teacher_list,many=True)
        return Response(teachers.data)
    else:
        teacher_info = TeacherFullInfoSerialzer(data = request.data)
        if teacher_info.is_valid():
            teacher_info.save()
            return Response(teacher_info.data,status=status.HTTP_201_CREATED)
        return Response(teacher_info.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET","PUT","DELETE"])
def TeacherInfo(request,teacher_id):
    def get_teacher_info(teacher_id):
        teacher_info= TeacherModel.objects.get(id=teacher_id)
        
        return teacher_info

    if request.method == "GET":
        teacher_info= get_teacher_info(teacher_id)
        teachers = TeacherFullInfoSerialzer(teacher_info)
        return Response(teachers.data)
    elif request.method=="PUT":
        teacher_info= get_teacher_info(teacher_id)
        teacher_serializer = TeacherFullInfoSerialzer(teacher_info,data=request.data)
        if teacher_serializer.is_valid():
            teacher_serializer.save()
            return Response(teacher_serializer.data,status=status.HTTP_200_OK)
        return Response(teacher_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    else:
        teacher_info= get_teacher_info(teacher_id)
        teacher_info.delete()
        msg = {"message":"deleted successfully"}
        return Response(msg,status=status.HTTP_200_OK)
        