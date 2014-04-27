from django.shortcuts import render, render_to_response
from django.template import RequestContext

from django.contrib.auth.decorators import login_required

from models import Challenge
from forms import ChallengeForm

@login_required(login_url='/login/')
def home(request):
    return render_to_response('home.html',
        {
        },
        context_instance=RequestContext(request))



@login_required(login_url='/login/')
def list(request):
    challenge = Challenge.objects.all()
    return render_to_response('challenges.html',
        {
            "challenge": challenge
        },
        context_instance=RequestContext(request))


@login_required(login_url='/login/')
def details(request, cause_id):
    challenge = Challenge.objects.get(pk=challenge_id)
    return render_to_response('challenge.html',
        {
            "challenge": challenge
        },
        context_instance=RequestContext(request))

@login_required(login_url='/login/')
def new(request):
    if request.method == 'POST':
        form = ChallengeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/challenges')
    else:
        form = ChallengeForm()
    return render_to_response('new_challenge.html',
        {
            "form": form
        },
        context_instance=RequestContext(request))

