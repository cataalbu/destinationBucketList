from django.shortcuts import render

from django.views import View

from destination.mvc.models.Destination import Destination

from destination.mvc.services.LoginRequieredMixin import LoginRequiredMixin
from destination.mvc.services.UserLoginRequired import UserLoginRequiredMixin
from destination.mvc.services.AdminLoginRequired import AdminLoginRequiredMixin

class GetPublicDestinationsView(LoginRequiredMixin):
    def get(self, request):
        destinations = Destination.objects.filter(is_public=True)
        context = {'destinations': destinations}
        return render(request, 'destination.html', context)