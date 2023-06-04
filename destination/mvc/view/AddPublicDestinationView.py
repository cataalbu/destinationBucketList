from django.shortcuts import render, redirect, resolve_url

# Create your views here.
from django.views import View

from destination.mvc.models.Destination import Destination
from destination.mvc.services.LoginRequieredMixin import LoginRequiredMixin
from destination.mvc.services.UserLoginRequired import UserLoginRequiredMixin
from destination.mvc.services.AdminLoginRequired import AdminLoginRequiredMixin


class AddPublicDestinationView(LoginRequiredMixin):
    def get(self, request):
        return render(request, 'add_public_destination.html')

    def post(self, request):
        geolocation = request.POST.get('geolocation')
        title = request.POST.get('title')
        image = request.POST.get('image')
        description = request.POST.get('description')
        is_public = True

        destination = Destination(geolocation=geolocation, title=title, image=image, description=description,
                                  arrival_date=None, departure_date=None, user_id=None, is_public=False)
        destination.save()

        return redirect(resolve_url('/public-destinations/'))
