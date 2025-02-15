from django.urls import path
from .views import home, plot, apply_filters

urlpatterns = [
    path('', home, name='home'),
    path('plot/', plot, name='plot'),
    path('apply-filters/', apply_filters, name='apply_filters'),
]
