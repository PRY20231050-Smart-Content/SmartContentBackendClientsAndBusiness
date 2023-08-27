# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import status
from django.db import connection
from django.core.paginator import Paginator, Page

#services view

class ClientSelectView(APIView):
      def post(self, request):
        try:
            user_id = request.data.get('user_id')
            with connection.cursor() as cursor:
                cursor.execute("""SELECT c.id, concat(c.first_name,' ',c.last_name) as name, c.created_at
                FROM clients c where c.user_id = %s """, [user_id])
                data = cursor.fetchall()
            if data:
                clients = [
                 {
                    'id': row[0],
                    'name': row[1],
                    'created_at': row[2],
                    
                 } for row in data
                ]

           
                return Response(clients, status=status.HTTP_200_OK)
            return Response({'message': 'No clients found.'}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

    
    
 