# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .db_operations import call_insert_client
from django.http import HttpResponse
from rest_framework import status

class ClientCreateView(APIView):
    def post(self, request):
        try:
            first_name = request.data.get('first_name')
            last_name = request.data.get('last_name')
            address_id = request.data.get('address_id')
            email = request.data.get('email')
            phone = request.data.get('phone')
            profile_picture = request.data.get('profile_picture')
            user_id = request.data.get('user_id')

            call_insert_client(first_name, last_name, address_id, email, phone, profile_picture, user_id)
            
            return Response({'message': 'Client created.'}, status=status.HTTP_201_CREATED)

        except Exception as e:
            # Puedes registrar la excepción aquí para depurarla posteriormente
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

