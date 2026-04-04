from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrReadOnly(BasePermission):
    """
    Lecture publique (GET, HEAD, OPTIONS).
    Ecriture (POST, PUT, PATCH, DELETE) reservee aux admins.
    """

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_staff


class IsAdminOrCreateOnly(BasePermission):
    """
    Permet la creation (POST) a tous + lecture aux admins.
    Utilise pour le formulaire de contact.
    """

    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        return request.user and request.user.is_staff
