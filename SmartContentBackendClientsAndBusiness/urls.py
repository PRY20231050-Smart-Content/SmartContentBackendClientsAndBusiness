"""SmartContentBackendClientsAndBusiness URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from SmartContentBackendClientsAndBusinessApp.views.client_views import ClientCreateView
from SmartContentBackendClientsAndBusinessApp.views.industry_views import IndustryCreateView
from SmartContentBackendClientsAndBusinessApp.views.address_views import AddressCreateView
from SmartContentBackendClientsAndBusinessApp.views.business_views import BusinessCreateView
from SmartContentBackendClientsAndBusinessApp.views.client_details_views import ClientCreateViewDetails


urlpatterns = [
  
    path('create-client/', ClientCreateView.as_view()),
    path('update-client/', ClientCreateView.as_view()),
    path('delete-client/', ClientCreateView.as_view()),
    path('get-all-clients/', ClientCreateView.as_view()),
    path('get-client-by-id/<int:client_id>/', ClientCreateViewDetails.as_view(), name='client-detail'),
    path('create-industry/', IndustryCreateView.as_view()),
    path('create-address/', AddressCreateView.as_view()),
    path('create-business/', BusinessCreateView.as_view()),
    path('update-business/', BusinessCreateView.as_view()),
]
