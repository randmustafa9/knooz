from django.urls import path
from strainger import views

urlpatterns=[

path('',views.redirectToHomee,name='toHome'),
path('home/',views.homee,name='inHome'),
path('whoAmI/',views.whoAmI,name='whoAmI'),
path('amI/',views.imI,name='amI'),
path('logout/',views.logoutt,name='logt'),


    
]

