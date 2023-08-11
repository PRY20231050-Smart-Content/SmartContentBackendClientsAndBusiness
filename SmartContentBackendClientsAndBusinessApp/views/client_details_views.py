# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import status
from django.db import connection
from django.core.paginator import Paginator, Page
from rest_framework.decorators import api_view


class ClientCreateViewDetails(APIView):
  
    def post(self, request):
        try:
            client_id = request.data.get('client_id')
            with connection.cursor() as cursor:
                cursor.execute("""SELECT clients.*, businesses.*  FROM clients LEFT JOIN businesses ON clients.id = businesses.client_id WHERE clients.id = %s """, [client_id])

                data = cursor.fetchone()

            if data:
                client_details = {
                    'id': data[0],
                    'first_name': data[1],
                    'last_name': data[2],
                    'address_id': data[3],
                    'email': data[4],
                    'phone': data[5],
                    'profile_picture': data[6],
                    'user_id': data[7],
                    # Include other fields as needed
                }

                return Response(client_details, status=status.HTTP_200_OK)

            return Response({'message': client_id}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
