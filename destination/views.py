from django.shortcuts import render, redirect, reverse, resolve_url

# Create your views here.
from django.views import View

from destination.models import Destination


class GetPublicDestinationsView(View):
    def get(self, request):
        destinations = Destination.objects.filter(is_public=True)
        context = {'destinations': destinations}
        return render(request, 'destination.html', context)


class AddPublicDestinationView(View):
    def get(self, request):
        return render(request, 'add_public_destination.html')

    def post(self, request):
        geolocation = request.POST.get('geolocation')
        title = request.POST.get('title')
        image = request.POST.get('image')
        description = request.POST.get('description')
        is_public = True

        destination = Destination(geolocation=geolocation, title=title, image=image, description=description,
                                  arrival_date=None, departure_date=None, user_id=None,  is_public=False)
        destination.save()

        return redirect(resolve_url('/public-destinations/'))
