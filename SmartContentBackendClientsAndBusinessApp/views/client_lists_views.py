# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import status
from django.db import connection
from django.core.paginator import Paginator, Page
from rest_framework.decorators import api_view


class ClientListView(APIView):
  
    def post(self, request):
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

            return Response({'message': 'No data found.'}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

