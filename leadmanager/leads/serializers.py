from rest_framework import serializers
from leads.models import Lead

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        # fields = (name, email .. )
        # can directly do this to add all fields
        fields = '__all__'

