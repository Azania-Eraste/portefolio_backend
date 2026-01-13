from rest_framework import serializers
from .models import (
    Utilisateur, Projet, Experience, Localisation,
    Service, ReseauSocial, PriseDeContact
)

class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = "__all__"


class ProjetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projet
        fields = "__all__"


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = "__all__"


class LocalisationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Localisation
        fields = "__all__"


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"


class ReseauSocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReseauSocial
        fields = "__all__"


class PriseDeContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriseDeContact
        fields = "__all__"
