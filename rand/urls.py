from django.urls import path
from rand import views

urlpatterns=[


path('',views.homer,name='homer'),
path('sheShouldKnow',views.sheSKnow,name='sheShouldKnowMe'),
path('msgSent',views.rMsgs,name='msgSentt'),
path('inbox',views.inboxR,name='inboxR'),
    
]