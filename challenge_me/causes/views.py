from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from models import Cause, CauseComment
from forms import CauseForm, CauseCommentForm
from challenges.models import Challenge


@login_required(login_url='/login/')
def list(request):
    causes = Cause.objects.all()
    return render_to_response('causes.html',
        {
            "causes": causes
        },
        context_instance=RequestContext(request))


@login_required(login_url='/login/')
def details(request, cause_id):
    cause = Cause.objects.get(pk=cause_id)
    challenges = Challenge.objects.filter(cause=cause)
    if request.method == 'POST':
        form = CauseCommentForm(request.POST)
        if form.is_valid():
            author = request.user
            comment = CauseComment()
            comment.author = author
            comment.text = form.cleaned_data['text']
            comment.cause = cause
            comment.save()
            return redirect('/causes/cause/' + str(cause.id))
    else:
        form = CauseCommentForm()

    comments = CauseComment.objects.all()
    return render_to_response('cause.html',
        {
            "cause": cause,
            "comment_form": form,
            "comments": comments,
            "challenges": challenges
        },
        context_instance=RequestContext(request))


@login_required(login_url='/login/')
def new(request):
    if request.method == 'POST':
        form = CauseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/causes')
    else:
        form = CauseForm()
    return render_to_response('new_cause.html',
        {
            "form": form
        },
        context_instance=RequestContext(request))
