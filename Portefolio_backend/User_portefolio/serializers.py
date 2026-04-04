from rest_framework import serializers
from .models import (
    Language, Utilisateur, Projet, Experience, Localisation,
    Service, ReseauSocial, PriseDeContact, Competence
)


class LocalisationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Localisation
        fields = "__all__"


class ServiceSerializer(serializers.ModelSerializer):
    localisation = LocalisationSerializer(read_only=True)

    class Meta:
        model = Service
        fields = "__all__"


class ExperienceSerializer(serializers.ModelSerializer):
    services = ServiceSerializer(many=True, read_only=True)

    class Meta:
        model = Experience
        fields = "__all__"


class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        exclude = ['password', 'is_superuser', 'is_staff', 'groups', 'user_permissions', 'last_login']


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = "__all__"


class CompetenceSerializer(serializers.ModelSerializer):
    categorie_display = serializers.CharField(source='get_categorie_display', read_only=True)
    niveau_display = serializers.CharField(source='get_niveau_display', read_only=True)

    class Meta:
        model = Competence
        fields = "__all__"


class ProjetSerializer(serializers.ModelSerializer):
    languages = LanguageSerializer(many=True, read_only=True)
    competences = CompetenceSerializer(many=True, read_only=True)

    class Meta:
        model = Projet
        fields = "__all__"


class ReseauSocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReseauSocial
        fields = "__all__"


class PriseDeContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriseDeContact
        fields = "__all__"
        read_only_fields = ['date_envoi']
