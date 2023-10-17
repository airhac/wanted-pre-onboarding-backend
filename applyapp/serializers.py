from .models import Apply
from rest_framework import serializers

class ApplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Apply
        fields = '__all__'