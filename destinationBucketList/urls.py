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

from destination.mvc.view.GetPublicDestinationsView import GetPublicDestinationsView
from destination.mvc.view.GetPrivateDestinationsView import GetPrivateDestinationsView
from destination.mvc.view.AddPublicDestinationView import AddPublicDestinationView
from destination.mvc.view.AddNewPrivateDestinationView import AddNewPrivateDestinationView
from destination.mvc.view.AuthenticationView import LoginView, LogoutView

urlpatterns = [
    path('', lambda request: redirect('/login/')),
    path('admin/', admin.site.urls),
    path('public-destinations/', GetPublicDestinationsView.as_view()),
    path('private-destinations/', GetPrivateDestinationsView.as_view()),
    path('add-public-destination/', AddPublicDestinationView.as_view(), name='add-public-destination'),
    path('add-new-private-destination/', AddNewPrivateDestinationView.as_view(), name='add-new-private-destination'),
    path('login/', LoginView.as_view(), name='LoginView'),
    path('logout/', LogoutView.as_view(), name='LogoutView'),
]
