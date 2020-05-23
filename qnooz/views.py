from django.shortcuts import render,redirect
from django.views.decorators.csrf import requires_csrf_token
from django.http import HttpResponse
import random
from django.http import HttpResponseRedirect
from .models import Kmsgs
from django.views.decorators.cache import never_cache
from django.contrib.auth import login, authenticate

# Create your views here.

# Create your views here.

 
 

@never_cache
@requires_csrf_token
def homee(request):
    if request.user.username == 'knooz':
        a = Kmsgs.objects.filter(msgtype=1, sender='rand', seen = False)
        aa = len(a)
        return render(request,'homeknooz.html', {'msgsnum':aa})
    else:
        return HttpResponseRedirect("/home/")

@requires_csrf_token
def uShouldKnowView(request):
    if request.user.username == 'knooz':
        fo = Kmsgs.objects.filter(msgtype=2, sender='rand').update(seen = True)
        foo = Kmsgs.objects.filter(msgtype=2)
        if len(foo) > 0:
            f = (random.choice(foo))
        else:
            f = 'there is nth u should know :('
        return render(request,'uShouldKnow.html', {'fi':f})
    else:
        return HttpResponseRedirect("/home/")

        #['I am infatuated with you.',
        #       'Im just thinking about what I could do to you. Do you want to know?',
        #       'The shower is such a lonely place. Care to join me?',
        #      'Im just thinking about what I could do to you. Do you want to know?',
        #          'I yearn for you.']


@requires_csrf_token
def kMsgs(request):
    if request.user.username == 'knooz':
        if request.method=='POST':
            commingmsg = request.POST.get('htmlMsg')
            reqMsg = Kmsgs(msgK=commingmsg, msgtype=1, sender=request.user.username)
            reqMsg.save()
            return render(request,'msgSentK.html')
        else:
            return render(request,'msgSentK.html',)
    else:
        return HttpResponseRedirect("/home/")




@requires_csrf_token
def inboxk(request):
    if request.user.username == 'knooz':
        kMsgL = Kmsgs.objects.filter(msgtype=1, sender='rand').update(seen = True)
        kMsgLl = Kmsgs.objects.filter(msgtype=1, sender='rand').order_by('-datek')
        return render(request, 'inboxk.html', {'li': kMsgLl})    
    else:
        return HttpResponseRedirect("/home/")