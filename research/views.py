from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from portfolio.forms import SymbolForm, AddPositionForm
from folio_viz.helpers.url_functions import get_fundamentals, get_realTime
from folio_viz.helpers.functions import cleanFinancialStatement
from portfolio.models import Portfolio
from datetime import datetime
import requests
import pandas as pd
import json
from django.utils.html import format_html




from django.http import HttpResponseRedirect
# def custom_redirect(url_name, *args, **kwargs):
#     from django.core.urlresolvers import reverse 
#     import urllib
#     url = reverse(url_name, args = args)
#     params = urllib.urlencode(kwargs)
#     return HttpResponseRedirect(url + "?%s" % params)







# MUST CHANGE IN PRODUCTION
api_key = '5cf16f2040e332.31358607'

# Name of variable in HTML template: variable passed
def research_home(request):
    
    
    # GET METHOD -----------------------------------------------------------------------------
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
                return HttpResponseRedirect(request.path_info)
             
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
        # messages.error(request, "Symbol not recognized. Please search again. Type \".TO\" for CAD symbols.", extra_tags='danger')
        # return HttpResponseRedirect(request.path_info)

    # POST METHOD -----------------------------------------------------------------------------
    if request.method == 'POST':
        updated_request = request.POST.copy()
        formSymbol = request.GET.get('symbol')
        formShares = request.POST.get('shares')
        formTransaction = request.POST.get('transaction_type')
        formPrice = request.POST.get('price')
        formPrice = str(round(float(formPrice), 2))
    
        updated_request.update({'symbol': formSymbol, 'price': formPrice})
        addPositionForm = AddPositionForm(updated_request)

        if addPositionForm.is_valid():     
            formPortfolio = addPositionForm.cleaned_data.get('portfolio')
            formShares = addPositionForm.cleaned_data.get('shares')
            formPrice = addPositionForm.cleaned_data.get('price')
            portfolioUrl = f'/portfolio/{formPortfolio.id}'

            # validate if portfolio has 20 or more positions
            if formPortfolio.position_set.count() >= 20:
                message = format_html(f' Portfolios have a maximum of <strong>20</strong> positions. \
                                            Please delete a position in portfolio <a href="{portfolioUrl}">{formPortfolio}</a> to add new securities.')
                messages.error(request, message , extra_tags='danger')
                return redirect('research_home') 

            # validate if symbol already exists in portfolio            
            # for position in formPortfolio.position_set.all():
            #     if position.symbol == formSymbol:
            #         formSymbol = formSymbol.upper()
            #         message = format_html(f'<strong>{formSymbol}</strong> already exists in portfolio <strong><a href="{portfolioUrl}">{formPortfolio}.</a></strong>\
            #                                     please update the quantity on the portfolio detail page.')
            #         messages.error(request, message , extra_tags='danger')
            #         return redirect('research_home')  

            addPositionForm.save()
            if 'BUY' in addPositionForm.cleaned_data.get('transaction_type'):
                formTransaction = 'ADDED'
            else:
                formTransaction = 'SOLD'

            formSymbol = formSymbol.upper()
            
            messages.success(request, f'{formShares} <strong>{formSymbol}</strong> \
                                        at <strong>${formPrice} {formTransaction}</strong> in portfolio <strong><a href="{portfolioUrl}">\
                                        {formPortfolio}.</a></strong>')
            return HttpResponseRedirect(request.path_info + f'?symbol={formSymbol}')
           



        return redirect('research_home') 



def charts(request):
    return render(request, 'research/charts.html')    
    
  
    


    