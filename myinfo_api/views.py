import logging

from django.conf import settings
from django.utils.crypto import get_random_string

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from myinfo.client import MyInfoPersonalClientV4

logger = logging.getLogger(__name__)


class MyInfoAuthView(APIView):
    def get(self, request):
        try:
            oauth_state = get_random_string(length=16)
            callback_url = settings.CALLBACK_URL

            client = MyInfoPersonalClientV4()
            auth_url = client.get_authorise_url(oauth_state, callback_url)        
            request.session['myinfo_oauth_state'] = oauth_state

            logger.info("Generated MyInfo auth URL successfully")
            return Response({
                'auth_url': auth_url,
                'state': oauth_state
            })
        except Exception as e:
            logger.error(f"Error generating auth URL: {str(e)}")
            return Response(
                {'error': 'Failed to generate authorization URL'}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class MyInfoCallbackView(APIView):
    def get(self, request):
        auth_code = request.query_params.get('code')
        oauth_state = request.session.get('myinfo_oauth_state')
        callback_url = settings.CALLBACK_URL

        if not auth_code:
            logger.error("No auth code provided in callback")
            return Response(
                {'error': 'Auth code is required'}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        if not oauth_state:
            logger.error("No oauth in session")
            return Response(
                {'error': 'Invalid session'}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            client = MyInfoPersonalClientV4()
            person_data = client.retrieve_resource(auth_code, oauth_state, callback_url)
            logger.info("Successfully retrieved MyInfo person data")
            return Response(person_data)

        except Exception as e:
            logger.error(f"Error retrieving person data: {str(e)}")
            return Response(
                {'error': str(e)}, 
                status=status.HTTP_400_BAD_REQUEST
            )
