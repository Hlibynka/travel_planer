import httpx
from rest_framework import serializers
from .models import Project, Place


class PlaceSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Place
        fields = ['id', 'external_id', 'notes', 'is_visited']


class ProjectSerializer(serializers.ModelSerializer):
    places = PlaceSerializer(many=True, required=False)

    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'start_date', 'is_completed', 'places']

    def validate_places(self, value):
        if len(value) > 10:
            raise serializers.ValidationError("Maximum 10 places per project.")
        return value

    def create(self, validated_data):
        places_data = validated_data.pop('places', [])

        project = Project.objects.create(**validated_data)

        for place_data in places_data:
            ext_id = place_data['external_id']

            # Перевірка в Art Institute API
            try:
                response = httpx.get(f"https://api.artic.edu/api/v1/artworks/{ext_id}", timeout=5.0)
                if response.status_code != 200:
                    raise serializers.ValidationError(f"Artwork ID {ext_id} is invalid.")
            except httpx.RequestError:
                raise serializers.ValidationError("Art Institute API is unreachable.")

            Place.objects.create(project=project, **place_data)

        return project