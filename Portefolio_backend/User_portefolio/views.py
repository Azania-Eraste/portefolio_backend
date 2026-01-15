from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import (
    Utilisateur, Projet, Experience, Localisation,
    Service, ReseauSocial, PriseDeContact, TypeDeProjet
)

from .serializers import (
    UtilisateurSerializer, ProjetSerializer, ExperienceSerializer,
    LocalisationSerializer, ServiceSerializer, ReseauSocialSerializer,
    PriseDeContactSerializer
)

class UtilisateurViewSet(ModelViewSet):
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer


class ProjetViewSet(ModelViewSet):
    queryset = Projet.objects.all()
    serializer_class = ProjetSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["type_de_projet"]

    @action(detail=False, methods=["get"], url_path="types")
    def types(self, request):
        """Retourne la liste des types de projet disponibles (clé + libellé)."""
        types = [{"key": tag.name, "label": tag.value} for tag in TypeDeProjet]
        return Response(types)


class ExperienceViewSet(ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer


class LocalisationViewSet(ModelViewSet):
    queryset = Localisation.objects.all()
    serializer_class = LocalisationSerializer


class ServiceViewSet(ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ReseauSocialViewSet(ModelViewSet):
    queryset = ReseauSocial.objects.all()
    serializer_class = ReseauSocialSerializer


class PriseDeContactViewSet(ModelViewSet):
    queryset = PriseDeContact.objects.all()
    serializer_class = PriseDeContactSerializer
