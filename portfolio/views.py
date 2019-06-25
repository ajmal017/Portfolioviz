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
from .models import Portfolio


# Name of variable in HTML template: variable passed
# def home(request):
#     context = {
#         'portfolios': Portfolio.objects.all()
#     }
    
#     return render(request, 'portfolio/home.html', context)

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
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Portfolio.objects.filter(user=user).order_by('-date_added')

class PortfolioDetailView(DetailView):
    model = Portfolio
    
class PortfolioCreateView(LoginRequiredMixin, CreateView):
    model = Portfolio
    fields = ['date_added', 'portfolio_name', 'portfolio_label']

    # setting author of the portfolio to logged in user
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PortfolioUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Portfolio
    fields = ['date_added', 'portfolio_name', 'portfolio_label']

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