from email import message
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from classBased.serializers import StudentInfoSerializer
from classBased.models import StudentInfoModel

# Create your views here.
class StudentInfoView(APIView):
    def post(self,request):
        serializer = StudentInfoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_200_OK)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
    def get(self,request):
        student_list = StudentInfoModel.objects.all()
        serializer = StudentInfoSerializer(student_list,many=True)
        return Response(serializer.data,status = status.HTTP_200_OK)

class StudentDetailView(APIView):
    def get_student_info(self,student_id):
        try:
            student_info = StudentInfoModel.objects.get(id=student_id)
            return student_info
        except StudentInfoModel.DoesNotExist as e:            
            raise e
    def get(self,request,student_id):
        try:
            student = self.get_student_info(student_id)
            serializer = StudentInfoSerializer(student)
            return Response(serializer.data,status = status.HTTP_200_OK)
        except:
            msg={"message":"No Record Found"}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
    def put(self,request,student_id):
        try:
            student = self.get_student_info(student_id)
            serializer = StudentInfoSerializer(student,data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status = status.HTTP_200_OK)
            return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
        except:
            msg={"message":"No Record Found"}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
    def delete(self,request,student_id):
        try:
            student = self.get_student_info(student_id)
            student.delete()
            msg={"message":"deleted successfully"}
            return Response(msg,status = status.HTTP_200_OK)
        except:
            msg={"message":"No Record Found"}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
