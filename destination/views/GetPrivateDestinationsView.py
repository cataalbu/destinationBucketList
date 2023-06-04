from django.shortcuts import render

from destination.models.User import User
from destination.models.Destination import Destination
from destination.mixins.UserLoginRequired import UserLoginRequiredMixin


class GetPrivateDestinationsView(UserLoginRequiredMixin):

    def get(self, request):
        user_id = request.session.get('user_id')
        is_admin = User.is_user_admin(user_id)
        destinations = Destination.objects.filter(user_id=user_id)
        context = {'destinations': destinations, 'is_admin': is_admin}
        return render(request, 'private_destination/private_destination_list.html', context)
