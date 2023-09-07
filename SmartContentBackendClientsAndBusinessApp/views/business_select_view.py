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
            where_condition = "1 = 1"

            if client_id is not None:
                where_condition = f"b.client_id = {client_id}"

            with connection.cursor() as cursor:
                cursor.execute( f"""
                    SELECT b.id, b.name, b.created_at
                    FROM businesses b
                    WHERE b.client_id = %s AND {where_condition}
                """, [client_id])
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
            return Response([], status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
     