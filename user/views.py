from rest_framework.views import APIView
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiResponse

from user import (
    serializers as user_serializers,
)

from error_seriaizer import ErrorSerializer

class UserView(APIView):
    @extend_schema(
        description='Cria um novo usuário',
        request=user_serializers.UserSerializerRequest,
        responses={
            201:OpenApiResponse(
                user_serializers.UserSerializerResponse,
                description="Retorna o usuário criado",
            ),
            400:OpenApiResponse(
                description='Erro durante a criação do usuário',
                response=ErrorSerializer,
            )
        }
    )
    def post(self, request: Request) -> Response:
        user_serialized = user_serializers.UserSerializerRequest(data=request.data)
        if not user_serialized.is_valid():
            return Response(ErrorSerializer({'error': user_serialized.errors}).data, status=status.HTTP_400_BAD_REQUEST)

        return Response(
            user_serializers.UserSerializerResponse(
                user_serialized.save()
            ).data,
            status=status.HTTP_201_CREATED
        )
