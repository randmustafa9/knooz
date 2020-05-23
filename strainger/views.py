from django.shortcuts import render,redirect
from django.views.decorators.csrf import requires_csrf_token
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
# Create your views here.




@requires_csrf_token
def redirectToHomee(request):
    return redirect('/home/')


@requires_csrf_token
def homee(request):
    return render(request,'homepage.html')


@requires_csrf_token
def whoAmI(request):
    if not request.user.is_authenticated:
        return render(request,'whoAmI.html')

    elif request.user.username == 'knooz':
        return HttpResponseRedirect("/knooz/")

    elif request.user.username == 'rand':
        return HttpResponseRedirect("/rand/")




@requires_csrf_token
def imI(request):
    msg = 'i smell human perfume :)...'
    msg2 = '403 Homo Sapiens are not allowed to access this website :)...'
    paswrd1 = request.POST.get('paswrd')
    
    if 'space1' in request.POST:
        user = authenticate(request, username='knooz', password=paswrd1)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect("/knooz/")  # Redirect to a success page.       
        else:
            return HttpResponse(msg, content_type='text/plain')    # Return an 'invalid login' error message.

    elif 'alien1' in request.POST:
        user = authenticate(request, username='rand', password=paswrd1)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect("/rand/")  # Redirect to a success page.       
        else:
            return HttpResponse(msg, content_type='text/plain')    # Return an 'invalid login' error message.

    elif 'human1' in request.POST:
        return HttpResponse(msg2, content_type='text/plain')

    else:
        return HttpResponseRedirect("/whoAmI/")

@requires_csrf_token
def logoutt(request):
    logout(request)
    return redirect('/home/')
