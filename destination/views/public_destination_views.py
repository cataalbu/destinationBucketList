from django.shortcuts import render, redirect, resolve_url
from django.views.generic import DetailView
from destination.models.destination import Destination
from destination.mixins.LoginRequiredMixin import LoginRequiredMixin
from destination.mixins.AdminLoginRequired import AdminLoginRequiredMixin
from django.shortcuts import get_object_or_404
from destination.models.user import User


class PublicDestinationDetailView(LoginRequiredMixin, DetailView):
    template_name = 'public_destination/public_destination_details.html'

    def get_queryset(self):
        user_id = self.request.session.get('user_id')
        return Destination.objects.filter(is_public=True)

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(self.get_queryset(), id=id_)


class PublicDestinationsListView(LoginRequiredMixin):
    @staticmethod
    def get(request):
        user_id = request.session.get('user_id')
        destinations = Destination.objects.filter(is_public=True)
        is_admin = User.is_user_admin(user_id)
        context = {'destinations': destinations, 'is_admin': is_admin}
        return render(request, 'public_destination/public_destination_list.html', context)


class PublicDestinationCreateView(AdminLoginRequiredMixin):
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