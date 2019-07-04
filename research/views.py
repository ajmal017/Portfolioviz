from django.shortcuts import render
from django.contrib import messages
from portfolio.forms import SymbolForm, AddPositionForm
from folio_viz.helpers.url_functions import get_fundamentals
import requests
import pandas as pd
import json

from portfolio.models import Portfolio




# https://eodhistoricaldata.com/api/fundamentals/AAPL.US?fmt=csv&api_token=5cf16f2040e332.31358607
# MUST CHANGE IN PRODUCTION
api_key = '5cf16f2040e332.31358607'

# Name of variable in HTML template: variable passed
def research_home(request):
    form = SymbolForm(request.GET or None)
    user_portfolios = Portfolio.objects.filter(user=request.user)
    
    # addPositionForm = AddPositionForm(initial={'shares': 100})
    addPositionForm = AddPositionForm(**{'user': request.user})
    
    
    print(user_portfolios)





    if form.is_valid():
        symbol = form['symbol'].value()
        response =  get_fundamentals(symbol, api_key)
        if response:  
            context = {
                'response': response,
                'addPositionForm': addPositionForm
            }
            
            return render(request, 'research/research_home.html', context)   
        else:
            messages.error(request, "Symbol not recognized. Please search again. Type \".TO\" for CAD symbols.", extra_tags='danger')
            return render(request, 'research/research_home.html')
    
    # DEFAULT PAGE
    url = 'https://eodhistoricaldata.com/api/fundamentals/gspc.indx?fmt=json&api_token={}'.format(api_key)      
    response = requests.get(url).json()
    if response:  
        context = {
            'response': response,
            'addPositionForm': addPositionForm
        }
        return render(request, 'research/research_home.html', context)
    messages.error(request, "Symbol not recognized. Please search again. Type \".TO\" for CAD symbols.", extra_tags='danger')
    return render(request, 'research/research_home.html')


    
    
def charts(request):
    return render(request, 'research/charts.html')    
    
  
    


    