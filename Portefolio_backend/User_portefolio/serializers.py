from rest_framework import serializers
from .models import (
    Utilisateur, Projet, Experience, Localisation,
    Service, ReseauSocial, PriseDeContact
)

# 1. Localisation (Niveau le plus bas)
class LocalisationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Localisation
        fields = "__all__"

# 2. Service (Dépend de Localisation)
class ServiceSerializer(serializers.ModelSerializer):
    # On imbrique l'objet complet Localisation au lieu d'avoir juste un ID
    localisation = LocalisationSerializer(read_only=True)

    class Meta:
        model = Service
        fields = "__all__"

# 3. Experience (Parent de Service)
class ExperienceSerializer(serializers.ModelSerializer):
    # CRUCIAL : On récupère la liste des services liés.
    # Le nom 'services' doit correspondre au related_name='services' défini dans ton models.py
    services = ServiceSerializer(many=True, read_only=True)

    class Meta:
        model = Experience
        fields = "__all__"

# 4. Les autres (Indépendants)
class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = "__all__"

class ProjetSerializer(serializers.ModelSerializer):
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