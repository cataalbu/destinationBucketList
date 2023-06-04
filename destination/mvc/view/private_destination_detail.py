from django.views.generic import DetailView
from destination.mvc.models.Destination import Destination
from destination.mvc.services.LoginRequieredMixin import LoginRequiredMixin
from django.shortcuts import get_object_or_404


class PrivateDestinationDetailView(LoginRequiredMixin, DetailView):
    template_name = 'private_destination_details.html'

    def get_queryset(self):
        user_id = self.request.session.get('user_id')
        return Destination.objects.filter(user_id=user_id, is_public=False)

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(self.get_queryset(), id=id_)
