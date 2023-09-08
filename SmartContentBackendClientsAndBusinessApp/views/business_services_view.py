from SmartContentBackendClientsAndBusinessApp.models import Service, ServiceBusiness
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class BusinessServicesView(APIView):
    def get(self, request, business_id):
        try:
            # Utiliza la función filter() para realizar la consulta.
            services = Service.objects.filter(servicebusiness__business_id=business_id)

            # Selecciona los campos que deseas obtener.
            services = services.values('id', 'name')

            # Convierte el resultado en una lista de diccionarios.
            service_list = list(services)

            return Response({'services': service_list}, status=status.HTTP_200_OK)

        except Exception as e:
            # Puedes registrar la excepción aquí para depurarla posteriormente
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
