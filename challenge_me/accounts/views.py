from django.shortcuts import redirect
from django.shortcuts import render

from django.contrib.auth import authenticate, login, logout

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect('/')
            # Redirect to a success page.
        else:
            print "Disabled Acc"
            # Return a 'disabled account' error message
    else:
        print "Invalid"
        # Return an 'invalid login' error message.


def logout_view(request):
    logout(request)
    return redirect('/')
