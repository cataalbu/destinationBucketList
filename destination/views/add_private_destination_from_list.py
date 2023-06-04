from django.shortcuts import render, redirect, resolve_url
from destination.models.Destination import Destination
from destination.mixins.UserLoginRequired import UserLoginRequiredMixin


class AddPrivateDestinationFromPublicView(UserLoginRequiredMixin):
    def get(self, request, id):
        return render(request, 'private_destination/add_from_public.html')

    def post(self, request, id):
        destination = Destination.objects.get(id=id)
        geolocation = destination.geolocation
        title = destination.title
        image = destination.image
        description = destination.description
        arrival_date = request.POST.get('arrival_date')
        departure_date = request.POST.get('departure_date')
        user_id = request.session.get('user_id')
        destination = Destination(geolocation=geolocation, title=title, image=image, description=description,
                                  arrival_date=arrival_date, departure_date=departure_date, user_id=user_id, is_public=False)
        destination.save()
        return redirect(resolve_url('/private-destinations/'))
