from rest_framework.permissions import BasePermission, IsAuthenticated

class IsAdminOrLibrarian(BasePermission):
    """
    Allow access only to users with role 'admin' or 'librarian'.
    """
    def has_permission(self, request, view):
        user = request.user
        return bool(user and user.is_authenticated and user.role in ['admin', 'librarian'])

