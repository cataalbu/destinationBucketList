from django.views.generic import DetailView
from destination.models.Destination import Destination
from destination.mixins.LoginRequiredMixin import LoginRequiredMixin
from django.shortcuts import get_object_or_404


class PublicDestinationDetailView(LoginRequiredMixin, DetailView):
    template_name = 'public_destination/public_destination_details.html'

    def get_queryset(self):
        user_id = self.request.session.get('user_id')
        return Destination.objects.filter(is_public=True)

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(self.get_queryset(), id=id_)
