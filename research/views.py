from django.shortcuts import render, redirect
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
    # addPositionForm = AddPositionForm(**{'user': request.user}, initial={'shares': 100, 'date': '2019-06-04', 'price': 2})
    data = {
        'shares': 100,
        'price': 10,
        'date': '2019-05-01',
        'commission': 4.99
    }

    if request.method == 'POST':
        # print(request.POST)
        updated_request = request.POST.copy()
        formSymbol = request.GET.get('symbol')

        formShares = request.POST.get('shares')
        formPrice = request.POST.get('price')
        formTransaction = request.POST.get('transaction_type')
 
        updated_request.update({'symbol': formSymbol})
        addPositionForm = AddPositionForm(updated_request)
        if addPositionForm.is_valid():
            addPositionForm.save()
            if 'BUY' in addPositionForm.cleaned_data.get('transaction_type'):
                formTransaction = 'BOUGHT'
            else:
                formTransaction = 'SOLD'
            formPortfolio = addPositionForm.cleaned_data.get('portfolio')
            formShares = addPositionForm.cleaned_data.get('shares')
            formPrice = addPositionForm.cleaned_data.get('price')
            formSymbol = formSymbol.upper()
            
            # username = addPositionForm.cleaned_data.get('username')
            messages.success(request, f'{formTransaction} {formShares} shares of\
                                        {formSymbol} at ${formPrice} in portfolio {formPortfolio}.')
            return redirect('research_home') 
    else:
        addPositionForm = AddPositionForm(**{'user': request.user}, initial=data)





    
    # Validate if SYMBOL form is valid
    if form.is_valid():
        symbol = form['symbol'].value()
        fundamentals =  get_fundamentals(symbol, api_key)
        realTime =  get_realTime(symbol, api_key)

        balanceSheetData = []
        
        
        for value in fundamentals['Financials']['Balance_Sheet']['yearly'].items():
            for k, v in value[1].items():
                if v is None:
                    value[1][k] = '-'
            
                try:
                    v = float(v)
                    value[1][k] = int(v / 1000000)
                except:
                    continue                
            balanceSheetData.append(value)    
            
                      
                
        # print(balanceSheetData)
                
        
                
                





        if fundamentals and realTime:  
            realTime['timestamp'] = datetime.fromtimestamp(realTime['timestamp'])
            realTime['change_p'] = float("{0:.2f}".format(realTime['change_p'] * 100))
            if realTime['change'] < 0:
                realTime['changeDown'] = True
         

            
                
                # if value is None:
                #     value = '-'
                # print(key)
                # balanceSheetData[key] = 'test'
                # print(balanceSheetData[key])
                # try:
                #     # print(type(value['totalLiab']))
                #     totalCurrentLiabilities = float(value['totalCurrentLiabilities'])
                #     accountsPayable = float(value['accountsPayable'])
                #     otherCurrentLiab = float(value['otherCurrentLiab'])
                #     shortLongTermDebt = float(value['shortLongTermDebt'])
                #     additionalLiabilities = totalCurrentLiabilities - (accountsPayable + otherCurrentLiab +shortLongTermDebt)
                # except:
                #     continue
                # value['otherCurrentLiab'] = str(float(value['otherCurrentLiab']) + additionalLiabilities)


            










            context = {
                'fundamentals': fundamentals,
                'addPositionForm': addPositionForm,
                'realTime': realTime,
                'balanceSheetData': balanceSheetData
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
    
  
    


    