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
                cursor.execute("""SELECT c.id, c.first_name, c.created_at, c.updated_at, ", cc ," cc,
                    JSON_ARRAYAGG(JSON_OBJECT('id', b.id, 'name', b.name,'service_name',i.name,'schedule',b.schedule,'created_at',b.created_at
                    ,'website',b.website,'target_audience',b.target_audience,'phone',b.phone,'mail',b.mail
                    ,'mission',b.mission,'vision',b.vision,'address',a.street,'facebook_page',b.facebook_page
                    ,'client_id',b.client_id,'industry_id',b.industry_id,'deleted_at',b.deleted_at,'updated_at',b.updated_at,'services',JSON_ARRAYAGG(JSON_OBJECT('idss', s.id))
                    )) AS businesses,
                    c.last_name ,c.email ,c.phone,concat_Ws(' ',a.street,a.country,a.city,a.postal_code) address,a.id address_id,
                    c.profile_picture
                    FROM clients c
                    LEFT JOIN businesses b ON c.id = b.client_id and b.deleted_at is null
                    left join address a on c.address_id=a.id
					left join industries i on i.id=b.industry_id
                    left join services_business sb on sb.business_id=b.id
                    left join services s on s.id=sb.service_id
                    WHERE c.deleted_at IS NULL and c.id = %s group by 1 """, [client_id])

                data = cursor.fetchone()

            if data:
                client_details = {
                    'id': data[0],
                    'first_name': data[1],
                    'created_at': data[2],
                    'updated_at': data[3],
                    'cc': data[4],
                    'business_id': data[5],
                    'last_name': data[6],
                    'email': data[7],
                    'phone': data[8],
                    'address' : data[9],
                    'address_id' : data[10],
                    'profile_picture': data[11],
                }

                return Response(client_details, status=status.HTTP_200_OK)

            return Response({'message': client_id}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
