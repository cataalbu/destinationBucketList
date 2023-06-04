from django.shortcuts import render

from destination.models.Destination import Destination
from destination.mixins.LoginRequiredMixin import LoginRequiredMixin
from destination.models.User import User


class PublicDestinationsListView(LoginRequiredMixin):
    @staticmethod
    def get(request):
        user_id = request.session.get('user_id')
        destinations = Destination.objects.filter(is_public=True)
        is_admin = User.is_user_admin(user_id)
        context = {'destinations': destinations, 'is_admin': is_admin}
        return render(request, 'public_destination/public_destination_list.html', context)
