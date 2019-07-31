from rest_framework import permissions

from rest_framework.exceptions import PermissionDenied


class IsAdmin(permissions.IsAdminUser):

    def has_permission(self, request, view):
        message = 'Not Owner'
        is_owner = bool(request.user and request.user.is_staff)
        if is_owner:
            return is_owner
        else:
            raise PermissionDenied(detail=message)


class OwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        message = 'You are not owner'
        if obj.rname == request.user:
            return True
        else:
            raise PermissionDenied(detail=message)


# class ResellerOwnerOrReadOnly(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         message = 'You are not owner'
#         if obj.reseller_name == request.reseller:
#             return True
#         else:
#             raise PermissionDenied(detail=message)


# if request.method in permissions.SAFE_METHODS:
#     return bool(obj.reseller == request.reseller)
# else:
#     raise PermissionDenied(detail=message)

# message = 'You are not owner'
# is_owner = bool(
#     request.method in permissions.SAFE_METHODS or
#     obj.reseller == request.reseller
# )
# if is_owner:
#     return is_owner
# else:
#     raise PermissionDenied(detail=message)


class IsAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        message = 'You Must Be Authenticated'
        is_it = bool(request.user and request.user.is_authenticated)
        if is_it:
            return is_it
        else:
            raise PermissionDenied(detail=message)
