# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import status
from django.db import connection
from django.core.paginator import Paginator, Page

class IndustryCreateView(APIView):
    def post(self, request):
        try:
            industry_name = request.data.get('name')
            with connection.cursor() as cursor:
                 cursor.execute("CALL insert_industry(%s)", [industry_name])
            
            return Response({'message': 'Industry created.'}, status=status.HTTP_201_CREATED)

        except Exception as e:
            # Puedes registrar la excepción aquí para depurarla posteriormente
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def put(self, request):
        try:
            id = request.data.get('id')
            name = request.data.get('name')
            with connection.cursor() as cursor:
                  cursor.execute("CALL update_industry(%s, %s)", [id, name])
            
            return Response({'message': 'Industry updated.'}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request):
        try:
            id = request.data.get('id')
            with connection.cursor() as cursor:
                 cursor.execute("CALL delete_industry(%s)", [id])
            
            return Response({'message': 'Industry deleted.'}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
