from django.shortcuts import render
from mixinBased.models import UserInfo
from mixinBased.serializers import UserInfoSerializers
from rest_framework import generics, mixins

# Create your views here.
class UserInfoList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset=UserInfo.objects.all()
    serializer_class = UserInfoSerializers

    def get(self,request):
        return self.list(request)

    def post(self,request):
        return self.create(request)

class UserDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset=UserInfo.objects.all()
    serializer_class = UserInfoSerializers

    def get(self,request,pk):
        return self.retrieve(request,pk)

    def put(self,request,pk):
        return self.update(request,pk)

    def delete(self,request,pk):
        return self.destroy(request,pk)
