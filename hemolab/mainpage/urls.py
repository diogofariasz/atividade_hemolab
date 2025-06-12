from django.urls import path
from mainpage.views import *

urlpatterns = [
    path('main/', main_view, name='main'),
    path('pag1/', pag1_view, name='pag1'),
    path('pag2/', pag2_view, name='pag2'),
]