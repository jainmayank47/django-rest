from django.shortcuts import render
from django.http import JsonResponse
from firstApp.models import studentModel



# Create your views here.
def employeeView(request):
    # emp = {
    #     "name":"mayank",
    #     "id":101,
    #     "salary":150000
    # }
    data = studentModel.objects.all()
    # student =  {"students":list(data.values("id","name","email"))}
    student =  {"students":list(data.values())}
    return JsonResponse(student)