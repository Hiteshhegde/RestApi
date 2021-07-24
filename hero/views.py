from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics 
from rest_framework.views import APIView
from .serializers import HeroSerializer
from .models import Hero


# Create your views here.
def index(request):
	return render(request, 'index.html')

#Heroes List view 
class HeroList(generics.ListAPIView):

	queryset = Hero.objects.all()
	serializer_class = HeroSerializer

#Hero single detail view
class HeroDetail(generics.RetrieveAPIView):

	queryset = Hero.objects.all()
	serializer_class = HeroSerializer


#class HeroViewSet(viewsets.ModelViewSet):
	"""
	List all heroes here

	"""
	#def get(self, request, format=None):
	#queryset = Hero.objects.all().order_by('name')
	#serializer_class = HeroSerializer
		#return Response(serializer.data)






