from django.urls import path
from .views import (
    PortfolioListView,
    PortfolioDetailView,
    PortfolioCreateView,
    PortfolioUpdateView,
    PortfolioDeleteView,
    UserPortfolioListView,
)
from . import views

urlpatterns = [
    path('home/', PortfolioListView.as_view(), name='portfolio-home'),
    path('', views.dashboard, name='portfolio-dashboard'),
    path('portfolios/<str:username>', UserPortfolioListView.as_view(), name='user-portfolios'),
    path('portfolio/<int:pk>/', PortfolioDetailView.as_view(), name='portfolio-detail'),
    path('portfolio/<int:pk>/update/', PortfolioUpdateView.as_view(), name='portfolio-update'),
    path('portfolio/<int:pk>/delete/', PortfolioDeleteView.as_view(), name='portfolio-delete'),
    path('portfolio/new/', PortfolioCreateView.as_view(), name='portfolio-create'),
    path('about/', views.about, name='portfolio-about'),
]