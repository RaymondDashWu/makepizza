from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from pizza.models import Pizza, Topping, PizzaTopping
from .serializers import PizzaToppingSerializer

class PizzaList(APIView):
   def get(self, request):
       pizzas = PizzaTopping.objects.all()[:20]
       data = PizzaToppingSerializer(pizzas, many=True).data
       return Response(data)

class PizzaDetail(APIView):
    def get(self, request, pk):
        pizza = get_object_or_404(PizzaTopping, pk = pk)
        data = PizzaToppingSerializer(pizza).data
        return Response(data)