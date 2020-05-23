from django.urls import path
from qnooz import views

urlpatterns=[


path('',views.homee,name='homee'),
path('uShouldKnow',views.uShouldKnowView,name='uShouldKnowname'),
path('sendMsg',views.kMsgs,name='kMsgs'),
path('inbox',views.inboxk,name='inboxk'),

    
]