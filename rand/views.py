from django.shortcuts import render,redirect
from django.views.decorators.csrf import requires_csrf_token
from django.http import HttpResponse
import random
from django.http import HttpResponseRedirect
from qnooz.models import Kmsgs
from django.views.decorators.cache import never_cache
# Create your views here.

@never_cache
@requires_csrf_token
def homer(request):
    if request.user.username == 'rand':
        a = Kmsgs.objects.filter(msgtype=1, sender='knooz', seen = False)
        aa = len(a)
        return render(request,'homeRand.html', {'msgsnum':aa})
    else:
        return HttpResponseRedirect("/home/")

 

@requires_csrf_token
def sheSKnow(request):
    if request.user.username == 'rand':
        if request.method=='POST':
            commingmsg = request.POST.get('htmlSKnow')
            addM = Kmsgs(msgK=commingmsg, msgtype=2, sender=request.user.username)
            addM.save()
            return render(request,'SheSentr.html')
        else:
            return render(request,'SheSentr.html',)
    else:
        return HttpResponseRedirect("/home/")


@requires_csrf_token
def rMsgs(request):
    if request.user.username == 'rand':
        if request.method=='POST':
            commingmsg = request.POST.get('htmlmsg2')
            addM = Kmsgs(msgK=commingmsg, msgtype=1, sender=request.user.username)
            addM.save()
            return render(request,'Sentr.html')
        else:
            return render(request,'Sentr.html',)
    else:
        return HttpResponseRedirect("/home/")



@requires_csrf_token
def inboxR(request):
    if request.user.username == 'rand':
        rMsgL = Kmsgs.objects.filter(msgtype=1, sender='knooz').update(seen = True)
        rMsgLl = Kmsgs.objects.filter(msgtype=1, sender='knooz').order_by('-datek')
        return render(request, 'inboxR.html', {'li': rMsgLl})    
    else:
        return HttpResponseRedirect("/home/")