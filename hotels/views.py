from django.shortcuts import render, redirect
from .models import Hotel
from .forms import HotelForms
from .serializers import HotelSerializer
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.
# def home(request):
#     hotels = Hotel.objects.all()
#     serializer = HotelSerializer(hotels, many=True)
#     return JsonResponse({'hotels':serializer.data}, safe=False)
#     return render(request, 'home.html', {'hotels':serializer.data})

# @api_view(['GET','PUT','DELETE', 'POST'])
# def hotel_detail(request,id):
#     try:
#         hotel = Hotel.objects.get(id=id)
#     except hotel.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'GET':
#         serializer = HotelSerializer(hotel)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = HotelSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

#     elif request.method == 'PUT':
#         serializer = HotelSerializer(hotel, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         hotel.delete()
#     else:
#         return render(request, 'home.html')

def home(request):
    hotel = Hotel.objects.all()
    serializer = HotelSerializer(hotel, many=True)
    return JsonResponse(serializer.data, safe=False)


def add(request):
    if request.method == 'POST':
        name = request.POST['name']
        loc = request.POST['location']
        rate = request.POST['rate']

        hotel = Hotel.objects.create(name=name, location=loc, rate=rate)
        hotel.save()
        return redirect()
    return render(request, 'add.html')

@api_view(['GET', 'PUT', 'DELETE'])
def hotel_detail(request, id):
    try:
        hotel = Hotel.objects.get(id=id)
    except hotel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = HotelSerializer(hotel)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = HotelSerializer(hotel, request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        hotel.delete()
    