from django.urls import path

from .views import ApiTest, Home

urlpatterns = [
    path('', Home),
    path('api', ApiTest.as_view()),
    #path('<int:pk>/', ),
]


