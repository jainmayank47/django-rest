from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from django.http import JsonResponse
from generics_views.serializers import TechnologyInfoSerializers,FrameworkInfoSerializers,TechnologyInfoListSerializers
from generics_views.models import TechnologyInfo,FrameworkInfo
import json
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination

# Create your views here.
class CustomPaginationInfo(PageNumberPagination):
    page_size = 2
    # default_limit = 3
    #page_query_param = 'offset'

class CustomLimitPaginationInfo(LimitOffsetPagination):
    default_limit = 3
    limit_query_param = 'max'
    offset_query_param = 'pageno'
    

class TechnologyInfoListView(generics.ListCreateAPIView):
    serializer_class = TechnologyInfoListSerializers
    queryset = TechnologyInfo.objects.all()
    pagination_class = CustomPaginationInfo
    
    def get(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = TechnologyInfo.objects.all()
        paginator = CustomLimitPaginationInfo()
        result_page = self.paginate_queryset(queryset)
        serializer = TechnologyInfoListSerializers(result_page,many=True)
        #return self.get_paginated_response(serializer.data)
        return Response(serializer.data)

    # def paginate_queryset(self, queryset, request, view=None):
    #     queryset = self.queryset()
    #     paginator = CustomLimitPaginationInfo()
    #     result_page = paginator.paginate_queryset(queryset,request)
    #     serializer = TechnologyInfoListSerializers(result_page,many=True)
    #     return get_paginated_response(self, serializer.data)


class TechnologyDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TechnologyInfoSerializers
    queryset = TechnologyInfo.objects.all()

class FrameworkInfoView(generics.ListCreateAPIView):
    serializer_class = FrameworkInfoSerializers
    queryset = FrameworkInfo.objects.all()

    # def post(self,request):
    #     #print(request.data.__len__)
    #     print(type(request.data))
    #     data = request.data
    #     #print(data)
    #     technology_id = data["technology"]
    #     print(technology_id)
    #     request.data["technology_id"] = technology_id
    #     print(request.data)
    #     return self.create(request)

class TechnologyInfoViewSet(viewsets.ModelViewSet):
    serializer_class = TechnologyInfoSerializers
    queryset = TechnologyInfo.objects.all()

