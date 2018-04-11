from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from record import views

app_name = 'record'
urlpatterns = [
	path('pigeon/', views.PigeonList.as_view(), name='pigeon_list'),
	path('pigeon/<int:pk/>', views.PigeonDetail.as_view(), name='pigeon_detail'),
	path('family/', views.PigeonfamilyList.as_view(), name='pigeonfamily_list'),
	path('family/<int:pk>', views.PigeonfamilyDetail.as_view(), name='pigeonfamily_detail'),
	path('familymember/<my_name>/', views.PigeonfamilymemberList.as_view(), name='pigeonfamilymember_list'),
]
