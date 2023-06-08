from django.shortcuts import render, redirect, resolve_url
from destination.models.destination import Destination
from destination.mixins.auth_mixins import UserLoginRequiredMixin
from destination.models.user import User
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404
from destination.forms import PrivateDestinationForm, PrivateDestinationFromPublicForm



class PrivateDestinationCreateFromPublicView(UserLoginRequiredMixin):

    def get(self, request, id):
        form = PrivateDestinationFromPublicForm()
        context = {'form': form, 'is_admin': False}
        return render(request, 'private_destination/add_from_public.html', context)

    @staticmethod
    def post(request, id):
        form = PrivateDestinationFromPublicForm(request.POST)
        context = {'form': form, 'is_admin': False}
        if form.is_valid():
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
        else:
            print('not valid')
            return render(request, 'private_destination/add_from_public.html', context)


class PrivateDestinationCreateView(UserLoginRequiredMixin):

    def get(self, request):
        form = PrivateDestinationForm()
        context = {'form': form, 'is_admin': False}
        return render(request, 'private_destination/add_private_destination.html', context)

    def post(self, request):
        form = PrivateDestinationForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            geolocation = request.POST.get('geolocation')
            title = request.POST.get('title')
            image = request.POST.get('image')
            description = request.POST.get('description')
            arrival_date = request.POST.get('arrival_date')
            departure_date = request.POST.get('departure_date')
            user_id = request.session.get('user_id')
            destination = Destination(geolocation=geolocation, title=title, image=image, description=description,
                                      arrival_date=arrival_date, departure_date=departure_date, user_id=user_id,
                                      is_public=False)
            destination.save()
            return redirect(resolve_url('/private-destinations/'))
        else:
            print('not valid')
            return render(request, 'private_destination/add_private_destination.html', context)


class PrivateDestinationListView(UserLoginRequiredMixin):

    def get(self, request):
        user_id = request.session.get('user_id')
        is_admin = User.is_user_admin(user_id)
        destinations = Destination.objects.filter(user_id=user_id)
        context = {'destinations': destinations, 'is_admin': is_admin}
        return render(request, 'private_destination/private_destination_list.html', context)


class PrivateDestinationDetailView(UserLoginRequiredMixin, DetailView):
    template_name = 'private_destination/private_destination_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # get the default context data
        context['is_admin'] = False  # add extra data to the context
        return context

    def get_queryset(self):
        user_id = self.request.session.get('user_id')
        return Destination.objects.filter(user_id=user_id, is_public=False)

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(self.get_queryset(), id=id_)
