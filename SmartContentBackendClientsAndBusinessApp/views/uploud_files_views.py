# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
import pandas as pd

from SmartContentBackendClientsAndBusinessApp.models import Copies

class UploadFileView(APIView):
    parser_classes = (MultiPartParser,)

    def post(self, request, *args, **kwargs):
        file = request.FILES.get('file')
        business_id = request.data.get('business_id')  # Assuming 'business_id' is sent from the frontend
        
        if file and business_id:
            data = pd.read_excel(file)
            
            for index, row in data.iterrows():
                copy = Copies.objects.create(
                    title=row['Title'],  # Use 'Title' instead of 'title'
                    description=row['Description'],  # Use 'Description' instead of 'description'
                    business_id_id=business_id,
                    # Add other fields from the Excel as needed
                )
            
            return Response({'message': 'Archivo Excel procesado correctamente.'})
        else:
            return Response({'message': 'No se ha proporcionado archivo o business_id.'})
