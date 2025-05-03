from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from . models import Employer

class EmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = '__all__'
        read_only_fields = ['user', 'created__at']
