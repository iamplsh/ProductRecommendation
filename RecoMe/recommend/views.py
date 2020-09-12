from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
# Create your views here.

def list_of_recommendations(request):

    recommendations = {
        "restaurants": [
            {
                "restaurantId": "10",
                "name": "A2B",
                "city": "Btm Layout",
                "imageUrl": "www.google.com",
                "latitude": 20.027,
                "longitude": 30.0,
                "opensAt": "18:00",
                "closesAt": "23:00",
                "attributes": [
                    "Tamil",
                    "South Indian"
                ]
            },
            {
                "restaurantId": "11",
                "name": "A2B",
                "city": "Hsr Layout",
                "imageUrl": "www.google.com",
                "latitude": 20.027,
                "longitude": 30.0,
                "opensAt": "18:00",
                "closesAt": "23:00",
                "attributes": [
                    "Tamil",
                    "South Indian"
                ]
            }
        ]
    }

    return JsonResponse(recommendations)

def index(request):
    return HttpResponse("This is Home")
