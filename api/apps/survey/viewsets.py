from rest_framework.viewsets import ModelViewSet


class IdModelViewSet(ModelViewSet):
    lookup_url_kwarg = 'id'
