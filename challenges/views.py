from django.shortcuts import render, HttpResponse
from django.http import HttpResponseNotFound, HttpResponseRedirect

# Create your views here.

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
months = [i.lower() for i in months]

def monthly_challenges(request, month):
    if month in months:
        return HttpResponse(f'you are at {month} month.')
    else:
        return HttpResponseNotFound(f'{month} is not a month')

def monthly_challenges_by_number(request, month):
    try: 
        months[month - 1]
        return HttpResponseRedirect(f'/challenges/{months[month-1]}')
    except: return HttpResponseNotFound(f'There is no {month} number of month')