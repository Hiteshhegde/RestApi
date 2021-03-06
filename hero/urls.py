from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from  . import views

#Adding routers 
#router = routers.DefaultRouter()
#router.register(r'hero', views.HeroViewSet , basename='hero')
#router.register(r'hero')

urlpatterns = []
urlpatterns += [
    path('', views.index,),
    path('hero/', views.HeroList.as_view()),
    path('hero/<int:pk>/', views.HeroDetail.as_view()),
    path('apiToken/', obtain_auth_token)
    #path('', include(router.urls)),
]   