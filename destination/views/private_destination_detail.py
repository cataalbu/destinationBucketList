from django.views.generic import DetailView
from destination.models.Destination import Destination
from destination.mixins.UserLoginRequired import UserLoginRequiredMixin
from django.shortcuts import get_object_or_404


class PrivateDestinationDetailView(UserLoginRequiredMixin, DetailView):
    template_name = 'private_destination/private_destination_details.html'

    def get_queryset(self):
        user_id = self.request.session.get('user_id')
        return Destination.objects.filter(user_id=user_id, is_public=False)

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(self.get_queryset(), id=id_)
