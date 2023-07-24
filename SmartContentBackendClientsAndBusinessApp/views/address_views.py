# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from ..db_operations import call_insert_address, call_update_address, call_delete_address
from django.http import HttpResponse
from rest_framework import status

class AddressCreateView(APIView):
    def post(self, request):
        try:
            city = request.data.get('city')
            country = request.data.get('country')
            postal_code = request.data.get('postal_code')
            street = request.data.get('street')
            call_insert_address(city, country, postal_code, street)
            
            return Response({'message': 'Address created.'}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request):
        try:
            id = request.data.get('id')
            city = request.data.get('city')
            country = request.data.get('country')
            postal_code = request.data.get('postal_code')
            street = request.data.get('street')
            call_update_address(id, city, country, postal_code, street)
            
            return Response({'message': 'Address updated.'}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request):
        try:
            id = request.data.get('id')
            call_delete_address(id)
            
            return Response({'message': 'Address deleted.'}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
