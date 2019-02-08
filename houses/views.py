from django.contrib.auth.models import User

from rest_framework import permissions, viewsets

from houses.models import House
from houses.permissions import IsOwnerOrReadOnly
from houses.serializers import HouseSerializer, UserSerializer


class HouseViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = House.objects.all()
    serializer_class = HouseSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
