from django.shortcuts import render

from django.contrib.auth.decorators import login_required



@login_required(login_url='/login/')
def list(request):
    return render_to_response('supporters.html',
        {
        },
        context_instance=RequestContext(request))


@login_required(login_url='/login/')
def details(request, cause_id):
    return render_to_response('supporter.html',
        {
        },
        context_instance=RequestContext(request))
