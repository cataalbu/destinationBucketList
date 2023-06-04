from django.shortcuts import render, redirect, resolve_url
from destination.models.destination import Destination
from destination.mixins.UserLoginRequired import UserLoginRequiredMixin
from destination.models.user import User
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404



class PrivateDestinationCreateFromPublicView(UserLoginRequiredMixin):

    def get(self, request, id):
        return render(request, 'private_destination/add_from_public.html')

    @staticmethod
    def post(request, id):
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


class PrivateDestinationCreateView(UserLoginRequiredMixin):

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


class PrivateDestinationListView(UserLoginRequiredMixin):

    def get(self, request):
        user_id = request.session.get('user_id')
        is_admin = User.is_user_admin(user_id)
        destinations = Destination.objects.filter(user_id=user_id)
        context = {'destinations': destinations, 'is_admin': is_admin}
        return render(request, 'private_destination/private_destination_list.html', context)


class PrivateDestinationDetailView(UserLoginRequiredMixin, DetailView):
    template_name = 'private_destination/private_destination_details.html'

    def get_queryset(self):
        user_id = self.request.session.get('user_id')
        return Destination.objects.filter(user_id=user_id, is_public=False)

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(self.get_queryset(), id=id_)
