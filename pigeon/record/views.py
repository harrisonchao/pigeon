from record.models import Pigeon, Pigeon_family
from record.serializers import PigeonSerializer, PigeonfamilySerializer
from rest_framework import generics
# Create your views here.


class PigeonList(generics.ListCreateAPIView):
	queryset = Pigeon.objects.all()
	serializer_class = PigeonSerializer

class PigeonDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Pigeon.objects.all()
	serializer_class = PigeonSerializer

class PigeonfamilyList(generics.ListCreateAPIView):
	queryset = Pigeon_family.objects.all()
	serializer_class = PigeonfamilySerializer

class PigeonfamilyDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Pigeon_family.objects.all()
	serializer_class = PigeonfamilySerializer
class PigeonfamilymemberList(generics.ListCreateAPIView):
	serializer_class = PigeonSerializer
	
	def get_queryset(self):
		request_name = self.kwargs.get('my_name')
		request_family = Pigeon.objects.get(name=request_name).family
		query=Pigeon_family.objects.get(name=request_family)
		return query.pigeon_set.all()
	
