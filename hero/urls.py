from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from hero import views


#router = routers.DefaultRouter()
#router.register(r'hero', views.HeroList)
#router.register(r'hero')

urlpatterns = [
    path('hero/', views.HeroList.as_view()),
    path('hero/<int:pk>/', views.HeroDetail.as_view()),
]