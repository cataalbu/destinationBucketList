from django.shortcuts import redirect, resolve_url
from django.views import View
from destination.mvc.models.User import Admin


class AdminLoginRequiredMixin(View):
    def dispatch(self, request, *args, **kwargs):
        user_id = request.session.get('user_id')
        if not user_id:
            return redirect(resolve_url('/login/'))

        # if the current user is not an admin
        if len(Admin.objects.filter(generaluser_ptr_id=user_id)) == 0:
            return redirect(resolve_url('/login/'))
        return super().dispatch(request, *args, **kwargs)
