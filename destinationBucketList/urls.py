"""
URL configuration for destinationBucketList project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path

from destination.view.PublicDestinationListView import PublicDestinationsListView
from destination.view.GetPrivateDestinationsView import GetPrivateDestinationsView
from destination.view.AddPublicDestinationView import AddPublicDestinationView
from destination.view.AddNewPrivateDestinationView import AddNewPrivateDestinationView
from destination.view.AuthenticationView import LoginView, LogoutView
from destination.view.private_destination_detail import PrivateDestinationDetailView
from destination.view.public_destination_detail import PublicDestinationDetailView

urlpatterns = [
    path('', lambda request: redirect('/login/')),
    path('admin/', admin.site.urls),
    path('public-destinations/', PublicDestinationsListView.as_view(), name='public_destination_list'),
    path('private-destinations/', GetPrivateDestinationsView.as_view(), name='private_destination_list'),
    path('private-destinations/<int:id>', PrivateDestinationDetailView.as_view(), name='private_destination_details'),
    path('public-destinations/<int:id>', PublicDestinationDetailView.as_view(), name='public_destination_details'),
    path('add-public-destination/', AddPublicDestinationView.as_view(), name='add_public_destination'),
    path('add-private-destination/', AddNewPrivateDestinationView.as_view(), name='add_private_destination'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
