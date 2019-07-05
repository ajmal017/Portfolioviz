from django.shortcuts import render
from django.contrib import messages
from portfolio.forms import SymbolForm, AddPositionForm
from folio_viz.helpers.url_functions import get_fundamentals, get_realTime
from portfolio.models import Portfolio
from datetime import datetime
import requests
import pandas as pd
import json

# MUST CHANGE IN PRODUCTION
api_key = '5cf16f2040e332.31358607'

# Name of variable in HTML template: variable passed
def research_home(request):
    # Create forms
    form = SymbolForm(request.GET or None)
    user_portfolios = Portfolio.objects.filter(user=request.user)
    addPositionForm = AddPositionForm(**{'user': request.user}, initial={'shares': 100})
    
    # Validate if symbol form is valid
    if form.is_valid():
        symbol = form['symbol'].value()
        fundamentals =  get_fundamentals(symbol, api_key)
        realTime =  get_realTime(symbol, api_key)
        if fundamentals and realTime:  
            realTime['timestamp'] = datetime.fromtimestamp(realTime['timestamp'])
            realTime['change_p'] = float("{0:.2f}".format(realTime['change_p'] * 100))
            if realTime['change'] < 0:
                realTime['changeDown'] = True
            context = {
                'fundamentals': fundamentals,
                'addPositionForm': addPositionForm,
                'realTime': realTime
            }
            return render(request, 'research/research_home.html', context)   
        else:
            messages.error(request, "Symbol not recognized. Please search again. Type \".TO\" for CAD symbols.", extra_tags='danger')
            return render(request, 'research/research_home.html')
    
    # DEFAULT SYMBOL GSPC      
    fundamentals =  get_fundamentals('gspc.indx', api_key)
    realTime =  get_realTime('gspc.indx', api_key)
    if fundamentals and realTime:  
        realTime['timestamp'] = datetime.fromtimestamp(realTime['timestamp'])
        realTime['change_p'] = float("{0:.2f}".format(realTime['change_p'] * 100))
        if realTime['change'] < 0:
            realTime['changeDown'] = True
        context = {
            'fundamentals': fundamentals,
            'addPositionForm': addPositionForm,
            'realTime': realTime
        }
        return render(request, 'research/research_home.html', context)
    messages.error(request, "Symbol not recognized. Please search again. Type \".TO\" for CAD symbols.", extra_tags='danger')
    return render(request, 'research/research_home.html')


    
    
def charts(request):
    return render(request, 'research/charts.html')    
    
  
    


    