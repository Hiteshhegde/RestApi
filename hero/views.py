from django.shortcuts import render
from django.http import HttpResponse, Http404
from rest_framework import viewsets 
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import HeroSerializer
from .models import Hero


# Create your views here.
def index(request):
	return HttpResponse("Hello , This is Heros")



class HeroList(APIView):
	"""
	List all heroes here

	"""
	def get(self, request, format=None):
		heroes = Hero.objects.all().order_by('name')
		serializer = HeroSerializer(heroes, many=True)
		return Response(serializer.data)


class HeroDetail(APIView):
	"""
	Detail  view of eachhero
	"""
	def get_object(self, pk):
		try:
			return Hero.objects.get(pk=pk)
		except Hero.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		hero = self.get_object(pk)
		serializer = HeroSerializer(hero)
		return Response(serializer.data)