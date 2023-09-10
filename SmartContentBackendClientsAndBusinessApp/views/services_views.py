# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import status
from django.db import connection
from django.core.paginator import Paginator, Page

#services view

class ServicesCreatView(APIView):
      def get(self, request):
        try:
            with connection.cursor() as cursor:
                cursor.execute("""SELECT s.id, s.name, s.created_at
                FROM services s;
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
            return Response({'message': 'No services found.'}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
      def post(self, request):
        try:
            # Obtén los datos del servicio del cuerpo de la solicitud
            service_name = request.data.get('name')
            service_description = request.data.get('description')
            service_created_by = request.data.get('created_by')

            # Define la consulta SQL para insertar un nuevo servicio
            sql_query = "INSERT INTO services (name, description,created_at,created_by) VALUES (%s, %s, now(), %s);"

            # Utiliza un cursor para ejecutar la consulta SQL
            with connection.cursor() as cursor:
                cursor.execute(sql_query, [service_name, service_description,service_created_by])

            # Confirma la transacción
            connection.commit()

            # Devuelve una respuesta de éxito
            return Response({'message': 'Service created.'}, status=status.HTTP_201_CREATED)

        except Exception as e:
            # Maneja cualquier excepción que pueda ocurrir durante la creación
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    
 