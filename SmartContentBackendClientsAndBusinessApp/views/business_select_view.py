# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import status
from django.db import connection
from django.core.paginator import Paginator, Page

#services view

class BusinessSelectView(APIView):
      def post(self, request):
        try:
            #pedir id de client
            client_id = request.data.get('clientId')
            with connection.cursor() as cursor:
                cursor.execute("""SELECT b.id, b.name, b.created_at
                FROM businesses b where b.client_id = %s """, [client_id])
                data = cursor.fetchall()
            if data:
                business = [
                 {
                    'id': row[0],
                    'name': row[1],
                    'created_at': row[2],
                    
                 } for row in data
                ]

           
                return Response(business, status=status.HTTP_200_OK)
            return Response({'message': 'No businesses found.'}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
     