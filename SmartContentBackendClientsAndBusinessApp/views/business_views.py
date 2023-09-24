# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import connection
import json
from SmartContentBackendClientsAndBusinessApp.helpers.upload_file import upload_file, get_file_url
from SmartContentBackendClientsAndBusinessApp.models.businesses import Business
import pandas as pd
from SmartContentBackendClientsAndBusinessApp.models import Copies

class BusinessCreateView(APIView):
    def post(self, request):
        try:
            name = request.data.get('name')
            facebook_page = request.data.get('facebook_page')
            services = request.data.get('services')
            services = json.loads(services) if services else []
            phone = request.data.get('phone')         
            address_id = request.data.get('address_id')
            website = request.data.get('website')
            mail = request.data.get('mail')
            industry_id = request.data.get('industry_id')
            schedule = request.data.get('schedule')        
            target_audience = request.data.get('target_audience')
            client_id = request.data.get('client_id')
            mission = request.data.get('mission')
            vision = request.data.get('vision')
            file_obj = request.data.get('image')
            file_name = ''
            if file_obj is not None:
                file_name = upload_file(file_obj)

            print('services ', type(services))
            
            
            with connection.cursor() as cursor:
                    cursor.execute("CALL insert_business(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s,%s)",
                       [name,facebook_page,json.dumps(services),phone,address_id, website, mail,industry_id,schedule,target_audience, client_id, mission,vision,file_name ])
                    namesss = cursor.fetchall()

                    excel_file = request.data.get('excel_copies')
                    last_business_created = Business.objects.latest('created_at')

                    print('excel_file ', excel_file)
                    
                    if excel_file and last_business_created:
                        data = pd.read_excel(excel_file)
                    
                        
                        
                        for index, row in data.iterrows():
                            copys = Copies.objects.create(
                                copy=row['Copy'],
                                likes=row['Likes'],
                                shared=row['Shared'],
                                flyer_text=row['Flyer Text'],
                                business_id=last_business_created,
                                # Add other fields from the Excel as needed
                            )

            return Response({'message': namesss}, status=status.HTTP_200_OK)

        except Exception as e:
            # You can log the exception here for debugging later
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request):
        try:
            business_id = request.data.get('business_id')
            name = request.data.get('name')
            facebook_page = request.data.get('facebook_page')
            services = request.data.get('services')
            services = json.loads(services) if services else []
            phone = request.data.get('phone')         
            address_id = request.data.get('address_id')
            website = request.data.get('website')
            mail = request.data.get('mail')
            industry_id = request.data.get('industry_id')
            schedule = request.data.get('schedule')        
            target_audience = request.data.get('target_audience')
            client_id = request.data.get('client_id')
            mission = request.data.get('mission')
            vision = request.data.get('vision')
            file_obj = request.data.get('image')
            file_name = ''
            if file_obj is not None:
                file_name = upload_file(file_obj)
        

            with connection.cursor() as cursor:
                      cursor.execute("CALL update_business(%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s,%s)", 
                       [business_id, name, facebook_page,json.dumps(services),phone,address_id, website, mail,industry_id,schedule,target_audience, client_id, mission,vision,file_name ])
                      namesss = cursor.fetchone()

            excel_file = request.data.get('excel_copies')

            if excel_file and business_id:
                data = pd.read_excel(excel_file)           
                        
                for index, row in data.iterrows():
                    copys = Copies.objects.create(
                        copy=row['Copy'],
                        likes=row['Likes'],
                        shared=row['Shared'],
                        flyer_text=row['Flyer Text'],
                        business_id_id=business_id,
                        # Add other fields from the Excel as needed
                        )

            return Response({'message': namesss}, status=status.HTTP_200_OK)

        except Exception as e:
            # You can log the exception here for debugging later
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

