from django.shortcuts import render


from destination.mvc.models.Destination import Destination
from destination.mvc.services.LoginRequieredMixin import LoginRequiredMixin


class GetPrivateDestinationsView(LoginRequiredMixin):

    def get(self, request):
        user_id = request.session.get('user_id')
        destinations = Destination.objects.filter(user_id=user_id)
        context = {'destinations': destinations}
        return render(request, 'private_destination_list.html', context)
