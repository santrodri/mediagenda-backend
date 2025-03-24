from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers

from drf_spectacular.utils import extend_schema, OpenApiResponse, OpenApiExample

from . import serializers as avatar_serializers
from . import  models

class ErrorSerializer(serializers.Serializer):
    error = serializers.CharField()

class AvatarView(APIView):
    @extend_schema(
        responses={200: avatar_serializers.AvatarResponseSerializer(many=True)},
        description='Busca todos os usuários',
    )

    def get(self, request: Request) -> Response:
        return Response(
            avatar_serializers.AvatarResponseSerializer(models.AvatarModel.objects.all(), many=True).data
        )

    @extend_schema(
        request=avatar_serializers.AvatarCreationSerializer,
        responses={
            201: OpenApiResponse(description='Avatar criado com sucesso', response=avatar_serializers.AvatarResponseSerializer),
            400:OpenApiResponse(
                description='Requisição mal formada',
                response=ErrorSerializer,
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
        serializer = avatar_serializers.AvatarCreationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)