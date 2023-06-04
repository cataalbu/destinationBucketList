from django.shortcuts import render, redirect, resolve_url
from django.contrib import messages

# Create your views here.
from django.views import View

from destination.mvc.models.Destination import Destination
from destination.mvc.models.User import GeneralUser, User, Admin

from django.core.exceptions import ObjectDoesNotExist
from django.contrib.sessions.backends.db import SessionStore

from destination.mvc.services.LoginRequieredMixin import LoginRequiredMixin
from destination.mvc.services.UserLoginRequired import UserLoginRequiredMixin
from destination.mvc.services.AdminLoginRequired import AdminLoginRequiredMixin


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        # check if the user exists, if doesn't is set to none
        # the case in which  multiple objects with
        # the same username and password exist is not treated
        try:
            user = GeneralUser.objects.get(username=username, password=password)
        except ObjectDoesNotExist:
            user = None

        if user is not None:
            # create a session for the user
            # the case in which there exist another type of user is not considered
            session = SessionStore()
            session['user_id'] = user.pk
            session.save()
            request.session['session_key'] = session.session_key
            request.session['user_id'] = user.pk

            if user.isAdmin:
                return redirect(resolve_url('/public-destinations/'))
            else:
                return redirect(resolve_url('/public-destinations/'))
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect(resolve_url('/login/'))


class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        session_key_to_destroy = request.session.session_key

        # Clear the session data for the specific session key
        request.session.flush()
        request.session.cycle_key()

        # Redirect to login page or any other desired page
        return redirect(resolve_url('/login/'))







