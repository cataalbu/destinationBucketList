from django.shortcuts import render

# Create your views here.
from django.views import View

from destination.models import Destination


class GetAllDestinationsView(View):
    def get(self, request):
        destinations = Destination.objects.all()
        context = {'destinations': destinations}
        return render(request, 'destination.html', context)