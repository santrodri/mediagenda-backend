from rest_framework import permissions
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from drf_spectacular.utils import extend_schema, OpenApiResponse, OpenApiExample

from . import (
    serializers as avatar_serializers,
    models as avatar_models
)

import error_seriaizer

class AvatarView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(
        description='Busca o seu avatar',
        responses={
            200: avatar_serializers.AvatarResponseSerializer,
            400: error_seriaizer.ErrorSerializer
        },

    )

    def get(self, request: Request) -> Response:
        try:
            return Response(
                avatar_serializers.AvatarResponseSerializer(
                    avatar_models.AvatarModel.objects.get(fk_user=request.user)
                ).data
            )
        except avatar_models.AvatarModel.DoesNotExist:
            return Response(error_seriaizer.ErrorSerializer({'error': 'usuário não possui um avatar'}).data, status=404)


    @extend_schema(
        request=avatar_serializers.AvatarCreationSerializer,
        responses={
            201: OpenApiResponse(description='Avatar criado com sucesso', response=avatar_serializers.AvatarResponseSerializer),
            400:OpenApiResponse(
                description='Requisição mal formada',
                response=error_seriaizer.ErrorSerializer,
                examples=[
                    OpenApiExample(
                        name='bad request',
                        value=dict(error='Requisição mal formada')
                    )
                ]
            ),
        },
        description='Adiciona um novo avatar',
    )
    def post(self, request: Request) -> Response:
        serializer = avatar_serializers.AvatarCreationSerializer(data=request.data, fk_user=request.user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)