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
        
    def get(self, request):
        try:
            with connection.cursor() as cursor:
                cursor.execute("""SELECT i.id, i.name, i.created_at
                FROM industries i;
                """)
                data = cursor.fetchall()
            if data:
                industries = [
                 {
                    'id': row[0],
                    'name': row[1],
                    'created_at': row[2],
                    
                 } for row in data
                ]

           
                return Response(industries, status=status.HTTP_200_OK)
            return Response({'message': 'No industries found.'}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)