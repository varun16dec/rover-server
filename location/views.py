from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from location.models import Location
from location.serializers import LocationSerializer
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.


class LocationList(APIView):

    @csrf_exempt
    def get(self,request):
        locations = Location.objects.all();
        serializer = LocationSerializer (locations, many=True)
        return Response({"data":serializer.data},status=status.HTTP_200_OK)

    @csrf_exempt
    def post(self,request):

        serializer = LocationSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)


class LocationLast(APIView):
    @csrf_exempt
    def get(self,request):
        last = Location.objects.last()
        serializer = LocationSerializer(last)
        return Response(serializer.data,status=status.HTTP_200_OK)

    @csrf_exempt
    def post(self,request):
        pass

