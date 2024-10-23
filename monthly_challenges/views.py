from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
def january(request):
    return HttpResponse("This is january !")

def february(request):
    return HttpResponse("This is february !")

def monthly_challenge(request, month):
    challenge_text=None
    if month=="january":
        challenge_text="This is january."
    elif month=="february":
        challenge_text="This is februar."
    elif month=="march":
        challenge_text="This is march."
    elif month=="april":
        challenge_text="This is april."
    elif month=="may":
        challenge_text="This is may."
    elif month=="june":
        challenge_text="This is june."
    elif month=="july":
        challenge_text="This is july."
    elif month=="august":
        challenge_text="This is august."
    elif month=="september":
        challenge_text="This is september."
    elif month=="octuber":
        challenge_text="This is octuber."
    elif month=="november":
        challenge_text="This is november."
    elif month=="december":
        challenge_text="This is december."
    else:
        return HttpResponseNotFound("This is not valid !")
    return HttpResponse(challenge_text)