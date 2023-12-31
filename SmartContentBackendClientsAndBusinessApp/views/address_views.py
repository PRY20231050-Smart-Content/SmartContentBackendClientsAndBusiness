# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import status
from django.db import connection
class AddressCreateView(APIView):
    def post(self, request):
        try:
            city = request.data.get('city')
            country = request.data.get('country')
            postal_code = request.data.get('postal_code')
            street = request.data.get('street')

            with connection.cursor() as cursor:
              cursor.execute("CALL insert_address(%s, %s, %s, %s)", [city, country, postal_code, street])
              data = cursor.fetchone()

            if data:
                address_details = {
                    'id': data[0],
                }
                
            return Response({'message': 'Address created.','id': address_details    }, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request):
        try:
            id = request.data.get('id')
            city = request.data.get('city')
            country = request.data.get('country')
            postal_code = request.data.get('postal_code')
            street = request.data.get('street')
            with connection.cursor() as cursor:
                  cursor.execute("CALL update_address(%s, %s, %s, %s, %s)", [id, city, country, postal_code, street])
            
            return Response({'message': 'Address updated.'}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request):
        try:
            id = request.data.get('id')
            with connection.cursor() as cursor:
                   cursor.execute("CALL delete_address(%s)", [id])

            
            return Response({'message': 'Address deleted.'}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
