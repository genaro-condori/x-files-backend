from rest_framework import generics
from django.contrib.auth import authenticate
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_200_OK
from rest_framework.views import APIView


# @api_view()
# def first_api_view(request):
#     numero_td = TipoDocumento.objects.count()
#     return Response({"numero_td": numero_td})

# @api_view()
# def all_tipo_documento(request):
#     lista = TipoDocumento.objects.all()
#     lista_serializer = CodigoDescripcionSerializer(lista, many=True)
#     return Response(lista_serializer.data)

class Login(APIView):

    def post(self, request):
        user = authenticate(username=request.data.get("username"), password=request.data.get("password"))
        if not user:
            return Response({'error': 'Credentials are incorrect or user does not exist'}, status=HTTP_404_NOT_FOUND)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=HTTP_200_OK)

