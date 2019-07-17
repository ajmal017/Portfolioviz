import requests
import pandas as pd
import json
from folio_viz.helpers.url_functions import get_eodQuote, get_realTime, get_bulkRealTime
from .models import Portfolio, Position
from pandas.io.json import json_normalize
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

api_key = '5cf16f2040e332.31358607'

# Name of variable in HTML template: variable passed


class PortfolioListView(ListView):
    model = Portfolio
    # <app> / <model>_<viewtype>.html is the name convention for templates
    template_name = 'portfolio/home.html' 
    # variable name that's looped over in the template
    context_object_name = 'portfolios'
    ordering = ['-date_added']
    paginate_by = 3

class UserPortfolioListView(ListView):
    model = Portfolio
    # <app> / <model>_<viewtype>.html is the name convention for templates
    template_name = 'portfolio/user_portfolios.html' 
    # variable name that's looped over in the template
    context_object_name = 'portfolios'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Portfolio.objects.filter(user=user).order_by('-date_added')

class PortfolioDetailView(DetailView):   
    model = Portfolio 
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        positions = self.get_object().position_set.all()
        realTimeQuotes = get_bulkRealTime(positions, api_key)
       
        temp = list(zip(realTimeQuotes, positions))
        marketValues = []
        changes = []
        percentageChanges = []
        for x in temp:
            marketValue = float("{0:.2f}".format(x[1].shares * x[0]['close']))
            marketValues.append(marketValue)
            change = float("{0:.2f}".format(marketValue - float(x[1].book_value)))
            changes.append(change)
            changePercentage = float("{0:.3f}".format( change / float(x[1].book_value )))
            percentageChanges.append(changePercentage)
        
        context['rtQuotes'] = list(zip(realTimeQuotes, positions, marketValues, changes, percentageChanges  ))
        print(context['rtQuotes'])
        return context
       
                




    
    

    
class PortfolioCreateView(LoginRequiredMixin, CreateView):
    model = Portfolio
    fields = ['date_added', 'portfolio_name', 'portfolio_label', 'description']

    # setting author of the portfolio to logged in user
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PortfolioUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Portfolio
    fields = ['date_added', 'portfolio_name', 'portfolio_label', 'description']

    # setting author of the portfolio to logged in user
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        portfolio = self.get_object()
        if self.request.user == portfolio.user:
            return True
        return False

class PortfolioDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Portfolio
    success_url = '/'
    
    def test_func(self):
        portfolio = self.get_object()
        if self.request.user == portfolio.user:
            return True
        return False

def about(request):
    return render(request, 'portfolio/about.html', {'title': 'About'})

# Name of variable in HTML template: variable passed
def dashboard(request):

    return render(request, 'portfolio/dashboard.html')