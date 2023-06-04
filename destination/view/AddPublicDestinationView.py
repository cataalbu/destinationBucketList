from django.shortcuts import render, redirect, resolve_url

# Create your views here.

from destination.models.Destination import Destination
from destination.mixins.AdminLoginRequired import AdminLoginRequiredMixin


class AddPublicDestinationView(AdminLoginRequiredMixin):
    def get(self, request):
        return render(request, 'public_destination/add_public_destination.html')

    def post(self, request):
        geolocation = request.POST.get('geolocation')
        title = request.POST.get('title')
        image = request.POST.get('image')
        description = request.POST.get('description')

        destination = Destination(geolocation=geolocation, title=title, image=image, description=description,
                                  arrival_date=None, departure_date=None, user_id=None, is_public=True)
        destination.save()

        return redirect(resolve_url('/public-destinations/'))
