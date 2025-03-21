from django.shortcuts import render
from django.views import View
import requests
from django.http import JsonResponse

class Home(View):
    def get(self, request):
        return render(request, 'index.html')
    
class TeamView(View):
    def get(self, request):
        
        return render(request, 'team.html')

class DwdView(View):
    '''
    All API endpoints with example are here: https://github.com/bundesAPI/dwd-api
    or use wetterdienst py library
    '''
    def get(self, request):
        return render(request, 'dwd.html')

class CoastWarningsDWDView(View):

    def get(self, request):
        if request.method == 'GET':
            data = {'message': 'Success!', 'key': 'value'}
            response = requests.get(url='https://s3.eu-central-1.amazonaws.com/app-prod-static.warnwetter.de/v16/sea_warning_text.json')
            # Decode the byte string to a regular string (UTF-8 decoding)
            decodedContent = response.content.decode('utf-8')

            # Optional: Remove the byte prefix (if necessary)
            # decoded_content = decoded_content.lstrip("b'").rstrip("'")

            # Replace any escape sequences like \" with " for proper HTML
            cleanedContent = decodedContent.replace('\\"', '"')
            cleanedContent = cleanedContent.replace('"', '')  # Remove all double quotes
            #print(cleanedContent)

            return JsonResponse({'html': cleanedContent})
        else:
            return JsonResponse({'error': 'Invalid request'}, status=400)

