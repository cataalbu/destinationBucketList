from django.shortcuts import redirect, resolve_url
from django.views import View
from destination.models.user import GeneralUser


class LoginRequiredMixin(View):

    def dispatch(self, request, *args, **kwargs):
        # if a user is not logged in, redirect him back to the login page
        session_key = request.session.get('session_key')
        # session =
        if not session_key:
            return redirect(resolve_url('/login/'))
        return super().dispatch(request, *args, **kwargs)


class AdminLoginRequiredMixin(View):

    def dispatch(self, request, *args, **kwargs):
        # if a user is not logged in, redirect him back to the login page
        session_key = request.session.get('session_key')
        user_id = request.session.get('user_id')
        # session =
        if not session_key:
            return redirect(resolve_url('/login/'))
        user = GeneralUser.objects.get(id=user_id)
        if not user.isAdmin:
            return redirect(resolve_url('/public-destinations/'))
        return super().dispatch(request, *args, **kwargs)


class UserLoginRequiredMixin(View):

    def dispatch(self, request, *args, **kwargs):
        # if a user is not logged in, redirect him back to the login page
        session_key = request.session.get('session_key')
        user_id = request.session.get('user_id')
        # session =
        if not session_key:
            return redirect(resolve_url('/login/'))
        user = GeneralUser.objects.get(id=user_id)
        if user.isAdmin:
            return redirect(resolve_url('/public-destinations/'))
        return super().dispatch(request, *args, **kwargs)

