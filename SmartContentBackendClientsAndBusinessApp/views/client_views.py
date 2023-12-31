# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import status
from django.db import connection
from django.core.paginator import Paginator, Page
from rest_framework.decorators import api_view
import json
from SmartContentBackendClientsAndBusinessApp.helpers.upload_file import upload_file, get_file_url
import uuid

class ClientCreateView(APIView):
    def post(self, request):
        try:
            first_name = request.data.get('first_name')
            last_name = request.data.get('last_name')
            address_id = request.data.get('address_id')
            email = request.data.get('email')
            phone = request.data.get('phone')
            user_id = request.data.get('user_id')
            profile_picture = request.data.get('profile_picture')
            profile_picture_file_name = ''
            
            if profile_picture is not None:
                profile_picture_file_name = upload_file(profile_picture)
            

            with connection.cursor() as cursor:
                 cursor.execute("CALL insert_client(%s, %s, %s, %s, %s, %s, %s)", [first_name, last_name, address_id, email, phone, profile_picture_file_name, user_id])
                 data = cursor.fetchone()

            if data:
                client_details = {
                    'id': data[0],
                    'first_name': data[1],
                    'created_at': data[2],
                    'updated_at': data[3],
                    'last_name': data[4],
                    'email': data[5],
                    'phone': data[6],
                    'address' : data[7],
                    'address_id' : data[8],
                    'profile_picture': data[9],
                }

            return Response({'message': 'Client created.','data': client_details}, status=status.HTTP_201_CREATED)

        except Exception as e:
            # Puedes registrar la excepción aquí para depurarla posteriormente
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request):
        try:
            client_id = request.data.get('client_id')
            first_name = request.data.get('first_name')
            last_name = request.data.get('last_name')
            address_id = request.data.get('address_id')
            email = request.data.get('email')
            phone = request.data.get('phone')
            profile_picture = request.data.get('profile_picture')
            profile_picture_file_name=''
            if profile_picture is not None:
                profile_picture_file_name = upload_file(profile_picture)
            user_id = request.data.get('user_id')

            with connection.cursor() as cursor:
                 cursor.execute("CALL update_client(%s, %s, %s, %s, %s, %s, %s, %s)", [client_id, first_name, last_name, address_id, email, phone, profile_picture_file_name, user_id])
            
            return Response({'message': 'Client updated.'}, status=status.HTTP_200_OK)

        except Exception as e:
            # Puedes registrar la excepción aquí para depurarla posteriormente
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


   
    def get(self, request):
        page = request.data.get('npage', 1)
        perpage = request.data.get('perPage', 10)
        sortby = request.data.get('sortBy', 'first_name')
        sortOrder = request.data.get('sortOrder', 'ASC')
        filterDateFrom = request.data.get('date_from')
        filterDateTo = request.data.get('date_to')
        text = request.data.get('text', '')
   
        params = [
            
            text,
            filterDateFrom,
            filterDateTo,
            perpage,
            page,
            sortby,
            sortOrder
            
        ]
      
        try:
            with connection.cursor() as cursor:
                cursor.callproc('sp_get_clients', params)
                data = cursor.fetchall()
                


            if data:
                paginator = Paginator(data, perpage)
                data_page = paginator.get_page(page)


                formatted_data = [
                 {
                    'id': row[0],
                    'first_name': row[1],
                    'created_at': row[2],
                    'updated_at': row[3],
                    'cc': row[4],
                    'business_id': row[5],
                    'last_name': row[6],
                    'email': row[7],
                    'phone': row[8],
                    'address' : row[9],
                    'address_id' : row[10],
                    'profile_picture': row[11],
                    
                 } for row in data
                ]

                result = {
                    'current_page': data_page.number,
                    'data': formatted_data,
                    'first_page_url': request.build_absolute_uri(f'?page=1'),
                    'from': data_page.start_index(),
                    'last_page': data_page.paginator.num_pages,
                    'last_page_url': request.build_absolute_uri(f'?page={data_page.paginator.num_pages}'),
                    'next_page_url': request.build_absolute_uri(data_page.next_page_number()) if data_page.has_next() else None,
                    'path': request.path,
                    'per_page': perpage,
                    'prev_page_url': request.build_absolute_uri(data_page.previous_page_number()) if data_page.has_previous() else None,
                    'to': data_page.end_index(),
                    'total': data[0][-1]  # as the total count is the last element of each row
                }

                return Response(result, status=status.HTTP_200_OK)

            return Response({'message': 'No data found.'}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

