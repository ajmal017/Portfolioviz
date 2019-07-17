from django.shortcuts import render, redirect
from django.contrib import messages
from portfolio.forms import SymbolForm, AddPositionForm
from folio_viz.helpers.url_functions import get_fundamentals, get_realTime
from folio_viz.helpers.functions import cleanFinancialStatement
from portfolio.models import Portfolio
from datetime import datetime
import requests
import pandas as pd
import json


# MUST CHANGE IN PRODUCTION
api_key = '5cf16f2040e332.31358607'

# Name of variable in HTML template: variable passed
def research_home(request):
        
    if request.method == 'GET': 
        symbol = request.GET.get('symbol')
        if symbol:
            fundamentals =  get_fundamentals(symbol, api_key)
            realTime =  get_realTime(symbol, api_key)

            if fundamentals and realTime:  
                today = datetime.today().strftime('%Y-%m-%d')
                try:
                    bv =  float("{0:.2f}".format(100 * float(realTime['close']) + 4.99))
                except:
                    bv = '-'
                data = {
                'shares': 100,
                'price': realTime['close'],
                'date': today,
                'commission': 4.99,
                'book_value': bv,
                }
                context = {
                    'fundamentals': fundamentals
                }

                if 'Common Stock' in fundamentals['General']['Type']:
                    try:
                        context['balanceSheetYearly'] = cleanFinancialStatement(fundamentals['Financials']['Balance_Sheet']['yearly'])
                        context['balanceSheetQuarterly'] = cleanFinancialStatement(fundamentals['Financials']['Balance_Sheet']['quarterly'])
                        context['incomeStatementYearly'] = cleanFinancialStatement(fundamentals['Financials']['Income_Statement']['yearly'])
                        context['incomeStatementQuarterly']= cleanFinancialStatement(fundamentals['Financials']['Income_Statement']['quarterly'])
                        context['cashFlowYearly'] = cleanFinancialStatement(fundamentals['Financials']['Cash_Flow']['yearly'])
                        context['cashFlowQuarterly'] = cleanFinancialStatement(fundamentals['Financials']['Cash_Flow']['quarterly'])
                        realTime['timestamp'] = datetime.fromtimestamp(realTime['timestamp'])
                        realTime['change_p'] = float("{0:.2f}".format(realTime['change_p'] * 100))
                        if realTime['change'] < 0:
                            realTime['changeDown'] = True
                        context['realTime'] = realTime
                    except:
                        print('Error Retrieving Financial Data')


                if request.user.is_authenticated:
                    addPositionForm = AddPositionForm(**{'user': request.user}, initial=data)
                    context['addPositionForm'] = addPositionForm
                
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
                'realTime': realTime
            }
            return render(request, 'research/research_home.html', context)
        messages.error(request, "Symbol not recognized. Please search again. Type \".TO\" for CAD symbols.", extra_tags='danger')
        return render(request, 'research/research_home.html')

    if request.method == 'POST':
        updated_request = request.POST.copy()
        formSymbol = request.GET.get('symbol')
        formShares = request.POST.get('shares')
        formTransaction = request.POST.get('transaction_type')
        formPrice = request.POST.get('price')
        formPrice = str(round(float(formPrice), 2))
        
        
        updated_request.update({'symbol': formSymbol, 'price': formPrice})

        addPositionForm = AddPositionForm(updated_request)
        print('form errors')
        print(addPositionForm.errors)
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
            
            messages.success(request, f'<strong>{formTransaction} {formShares}</strong> shares of\
                                        <strong>{formSymbol}</strong> at <strong>${formPrice}</strong> in portfolio <strong>{formPortfolio}.</strong>')
            return redirect('research_home') 
        return redirect('research_home') 


def charts(request):
    return render(request, 'research/charts.html')    
    
  
    


    