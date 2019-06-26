from django.shortcuts import render
from django.contrib import messages
from portfolio.forms import SymbolForm
import requests
import pandas as pd
import json




# https://eodhistoricaldata.com/api/fundamentals/AAPL.US?fmt=csv&api_token=5cf16f2040e332.31358607


# Name of variable in HTML template: variable passed
def research_home(request):
    
    api_key = '5cf16f2040e332.31358607'
    form = SymbolForm(request.POST or None)
    if form.is_valid():
        symbol = form['symbol'].value()
        url = 'https://eodhistoricaldata.com/api/fundamentals/{}?fmt=csv&api_token={}'.format(symbol, api_key)
        response = requests.get(url).json()
        if response:  
            context = {
                'response': response
            }
            return render(request, 'research/research_home.html', context)   
    messages.error(request, "Symbol not recognized. Please search again. Type \".TO\" for CAD symbols.", extra_tags='danger')
    return render(request, 'research/research_home.html')
    
    
    
    
  
    


    