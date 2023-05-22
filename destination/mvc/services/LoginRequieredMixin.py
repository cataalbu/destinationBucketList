from django.shortcuts import redirect, resolve_url
from django.views import View


class LoginRequiredMixin(View):
    def dispatch(self, request, *args, **kwargs):
        # if an user is not logged in, redirect him back to the login page
        session_key = request.session.get('session_key')
        # session =
        print(session_key)
        if not session_key:
            return redirect(resolve_url('/login/'))
        return super().dispatch(request, *args, **kwargs)