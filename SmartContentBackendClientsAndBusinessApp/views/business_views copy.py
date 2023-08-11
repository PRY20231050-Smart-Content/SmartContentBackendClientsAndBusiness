# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import connection
class BusinessCreateView(APIView):
    def post(self, request):
        try:
            name = request.data.get('name')
            target_audience = request.data.get('target_audience')
            experience_years = request.data.get('experience_years')
            reach_range = request.data.get('reach_range')
            phone = request.data.get('phone')
            address_id = request.data.get('address_id')
            website = request.data.get('website')
            mail = request.data.get('mail')
            industry_id = request.data.get('industry_id')
            schedule = request.data.get('schedule')
            copy_languages = request.data.get('copy_languages')
            client_id = request.data.get('client_id')
            mission = request.data.get('mission')
            vision = request.data.get('vision')
            values = request.data.get('values')

            with connection.cursor() as cursor:
                    cursor.execute("CALL insert_business(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", 
                       [name, target_audience, experience_years, reach_range, phone, 
                        address_id, website, mail, industry_id, schedule, 
                        copy_languages, client_id, mission, vision, values])
            
            return Response({'message': 'Business created.'}, status=status.HTTP_201_CREATED)

        except Exception as e:
            # You can log the exception here for debugging later
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request):
        try:
            business_id = request.data.get('business_id')
            name = request.data.get('name')
            target_audience = request.data.get('target_audience')
            experience_years = request.data.get('experience_years')
            reach_range = request.data.get('reach_range')
            phone = request.data.get('phone')
            address_id = request.data.get('address_id')
            website = request.data.get('website')
            mail = request.data.get('mail')
            industry_id = request.data.get('industry_id')
            schedule = request.data.get('schedule')
            copy_languages = request.data.get('copy_languages')
            client_id = request.data.get('client_id')
            mission = request.data.get('mission')
            vision = request.data.get('vision')
            values = request.data.get('values')

            with connection.cursor() as cursor:
                      cursor.execute("CALL update_business(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", 
                       [business_id, name, target_audience, experience_years, reach_range, phone, 
                        address_id, website, mail, industry_id, schedule, 
                        copy_languages, client_id, mission, vision, values])

            return Response({'message': 'Business updated.'}, status=status.HTTP_200_OK)

        except Exception as e:
            # You can log the exception here for debugging later
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

