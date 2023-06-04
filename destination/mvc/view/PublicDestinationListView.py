from django.shortcuts import render

from destination.mvc.models.Destination import Destination

from destination.mvc.services.LoginRequieredMixin import LoginRequiredMixin


class PublicDestinationsListView(LoginRequiredMixin):
    @staticmethod
    def get(request):
        destinations = Destination.objects.filter(is_public=True)
        context = {'destinations': destinations}
        return render(request, 'public_destination_list.html', context)
