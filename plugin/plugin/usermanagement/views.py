# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from plugin.usermanagement.utils import (get_all_users)
from plugin.usermanagement.forms import AddUserForm
from django.contrib.auth.models import User

def menu(request):
    """
        Purpose: To render user listing page
        Input: Http Request
        Returns: User listing page
        Dependency: NA
    """

    return render_to_response('usermanagement/index.html', {}, 
                          context_instance=RequestContext(request))

def view_users(request):
    """
        Purpose: To render user listing page
        Input: Http Request
        Returns: User listing page
        Dependency: NA
    """

    return render_to_response('usermanagement/users.html', {'users': get_all_users()}, 
                          context_instance=RequestContext(request))

def add_user(request):
    """
    """
    form_obj = AddUserForm()
    return render_to_response('usermanagement/add_user.html', {'form': form_obj}, 
                          context_instance=RequestContext(request))

def save_user(request):
    """
    """
    if request.method == "POST":
        form_obj = AddUserForm(request.POST)
        if form_obj.is_valid():

            username = form_obj.cleaned_data.get('username', None)
            first_name = form_obj.cleaned_data.get('first_name', None)
            last_name = form_obj.cleaned_data.get('last_name', None)
            password = form_obj.cleaned_data.get('password', None)

            user = User.objects.create_user(username, '', password)

            user.first_name = first_name
            user.last_name = last_name
            user.save()

            return HttpResponseRedirect("/plugin/users/")
        else:
            return render_to_response('usermanagement/add_user.html', {'form': form_obj}, 
                          context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect("/plugin/users/")