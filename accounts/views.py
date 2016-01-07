from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.template import RequestContext
from django.contrib import auth
from django.contrib.auth.decorators import login_required

from .models import Rockleton
from .forms import UserForm, RockletonForm

@login_required
def index(request):
    
    #Ed / c66
    
    context = {
        'message': '',
    }
    return render(request, 'accounts/index.html', context)
    
def register(request):
    if request.method == 'POST':
        uf = UserForm(request.POST, prefix='user')
        rf = RockletonForm(request.POST, prefix='rockleton')
        if uf.is_valid() * rf.is_valid():
            user = uf.save()
            rockleton = rf.save(commit=False)
            rockleton.user = user
            rockleton.save()
            return HttpResponseRedirect(index)
    else:
        uf = UserForm(prefix='user')
        rf = RockletonForm(prefix='rockleton')
    return render_to_response('accounts/register.html', 
                              dict(userform=uf,
                                   rockletonform=rf),
                              context_instance=RequestContext(request))