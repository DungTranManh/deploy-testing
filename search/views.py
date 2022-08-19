from django.shortcuts import render
from rest_framework import filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SearchSerializer
from .models import Data
from django.db.models import Q
# Create your views here.

def index(request):
    datas_search = request.GET.get('searchbar_value')
    checked_box = request.GET.get('flexRadioDefault')
    data = Data.objects.all()
    if checked_box == 'keb&reb':
        if datas_search:
            data = Data.objects.filter(Q(keb = datas_search) | Q(reb=datas_search))
        else:
            data = Data.objects.all()
    elif checked_box == 'keb':
        if datas_search:
            data = Data.objects.filter(Q(keb = datas_search))
        else:
            data = Data.objects.all()
    elif checked_box == 'reb':
        if datas_search:
            data = Data.objects.filter(Q(reb=datas_search))
        else:
            data = Data.objects.all()
    return render(request, 'search/index.html',{'datas':data})

class SearchAPIView_keb(APIView):
    def get(self,request,keb_text):
        data_get = Data.objects.get(keb = keb_text)
        if not data_get:
            return Response(data="can not get data", status=status.HTTP_400_BAD_REQUEST)
        else:
            data_get_serializer = SearchSerializer(data_get)
            return Response(data=data_get_serializer.data,status=status.HTTP_200_OK)

class SearchAPIView_reb(APIView):
    def get(self,request,reb_text):
        data_get = Data.objects.filter(reb = reb_text)
        if not data_get:
            return Response(data="can not get data", status=status.HTTP_400_BAD_REQUEST)
        else:
            data_get_serializer = SearchSerializer(data_get, many = True)
            return Response(data = data_get_serializer.data,status=status.HTTP_200_OK)


