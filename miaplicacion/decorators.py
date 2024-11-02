from functools import wraps
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib import messages

def role_required(allowed_roles):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if request.user.is_authenticated and hasattr(request.user, 'rol') and request.user.rol.nombre in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                messages.error(request, 'Acceso denegado.Usted no tiene permisos suficientes para acceder al recurso solicitado.')
                return redirect(reverse_lazy('acceso_denegado'))
        return wrapper
    return decorator