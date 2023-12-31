# serializers.py
from rest_framework import serializers
from .models import Branches


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branches
        fields = ['id', 'name', 'district_id']
