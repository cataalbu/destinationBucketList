from django.shortcuts import render, redirect, resolve_url
from destination.models.Destination import Destination
from destination.mixins.LoginRequiredMixin import LoginRequiredMixin


class AddNewPrivateDestinationView(LoginRequiredMixin):
    def get(self, request):
        return render(request, 'private_destination/add_private_destination.html')

    def post(self, request):
        geolocation = request.POST.get('geolocation')
        title = request.POST.get('title')
        image = request.POST.get('image')
        description = request.POST.get('description')
        arrival_date = request.POST.get('arrival_date')
        departure_date = request.POST.get('departure_date')
        user_id = request.session.get('user_id')
        destination = Destination(geolocation=geolocation, title=title, image=image, description=description,
                                  arrival_date=arrival_date, departure_date=departure_date, user_id=user_id, is_public=False)
        destination.save()
        return redirect(resolve_url('/private-destinations/'))
