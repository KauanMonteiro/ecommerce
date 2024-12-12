from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('vermaisproduto/<int:id>/',views.vermaisproduto, name='vermaisproduto')
]
