from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views
from .views import HelloViewSet

router = DefaultRouter()

router.register('profile', views.UserProfileViewSets)



urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view(), name='hello-view'),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls))
]
