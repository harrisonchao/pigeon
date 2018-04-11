from rest_framework import serializers
from record.models import Pigeon, Pigeon_family

class PigeonSerializer(serializers.ModelSerializer):
	class Meta:
		model = Pigeon
		fields = ('id', 'name', 'dad', 'mom', 'family')

class PigeonfamilySerializer(serializers.ModelSerializer):
	class Meta:
		model = Pigeon_family
		fields = ('id', 'name')
