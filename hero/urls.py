from django.urls import path, include
from rest_framework import routers
from  . import views

#Adding routers 
#router = routers.DefaultRouter()
#router.register(r'hero', views.HeroViewSet , basename='hero')
#router.register(r'hero')

#Url Patterns
urlpatterns = [
    path('hero/', views.HeroList.as_view()),
    path('hero/<int:pk>/', views.HeroDetail.as_view()),
    #path('', include(router.urls)),
]   