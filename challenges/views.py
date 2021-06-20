from django.shortcuts import render, HttpResponse
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
months = [i.lower() for i in months]

def monthly_challenges(request, month):
    if month in months:
        return HttpResponse(f'<h1 align="center">you are at {month} month.</h1>')
    else:
        return HttpResponseNotFound(f'<h1 align="center">{month} is not a month</h1>')

def monthly_challenges_by_number(request, month):
    try: 
        months[month - 1]
        return HttpResponseRedirect(reverse('month_challenge', args=[months[month - 1]]))
    except: return HttpResponseNotFound(f'<h1 align="center">There is no {month} number of month</h1>')