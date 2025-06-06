from rest_framework import generics
from rest_framework.response import Response
from .faker_generate_car import generate_car


# Create your views here.
class GenerateCarView(generics.ListAPIView):

    def get(self, request, *args, **kwargs):
        data = [generate_car() for _ in range(1)]
        return Response(data)
