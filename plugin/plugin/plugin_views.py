# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from plugin.usermanagement.utils import (get_all_users)

def index(request):
    """
        Purpose: To render main plugin page
        Input: Http Request
        Returns: Application plugin page
        Dependency: NA
    """

    return render_to_response('common/base.html', {}, 
                          context_instance=RequestContext(request))
