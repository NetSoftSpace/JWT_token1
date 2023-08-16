from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .serializer import RegistrationSerializer


@api_view(['POST', ])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)

        data = {}

        if serializer.is_valid():
            account = serializer.save()

            data['response'] = 'Successfully registered a new user.'
            data['username'] = account.username
            data['email'] = account.email

            token = RefreshToken.for_user(account)
            data['token'] = {
                'refresh': str(token),
                'access': str(token.access_token)
            }
        else:
            data = serializer.errors

        return Response(data)
