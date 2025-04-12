from random import randint
from datetime import datetime, timedelta

from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.reverse import reverse
from urllib.parse import urlencode

from drf_spectacular.utils import extend_schema, OpenApiResponse, OpenApiParameter
from drf_spectacular.types import OpenApiTypes

from . import (
    serializers as user_serializers,
    models as user_models,
    html_template as user_html_template
)

from error_seriaizer import ErrorSerializer


class UserView(APIView):
    @extend_schema(
        description='Cria um novo usuário',
        request=user_serializers.UserSerializerRequest,
        responses={
            201: OpenApiResponse(
                user_serializers.UserSerializerResponse,
                description="Retorna o usuário criado",
            ),
            400: OpenApiResponse(
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


class CodeView(APIView):
    @extend_schema(
        request=user_serializers.UserNonCofirmedSerializer,
        responses={204: OpenApiTypes.NONE, 400: ErrorSerializer}
    )

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name='code',
                type=OpenApiTypes.STR,
                description='A verification code',
                required=True
            )
        ],
        responses={204: None}
    )

    def get(self, request: Request) -> Response:
        code = request.GET.get('code')
        if not code:
            return Response(ErrorSerializer({'error': 'code is required'}).data, status=status.HTTP_400_BAD_REQUEST)

        if not user_models.CodeModel.objects.filter(email_code=code).exists():
            return Response(ErrorSerializer({'error': 'code is invalid'}).data, status=status.HTTP_400_BAD_REQUEST)

        modal_code = user_models.CodeModel.objects.get(email_code=code)

        if modal_code.created_at + timedelta(minutes=5) < datetime.now():
            return Response(ErrorSerializer({'error': 'code is invalid'}).data, status=status.HTTP_400_BAD_REQUEST)

        user = User(
            username = modal_code.fk_user_non_confirmed.username,
            email = modal_code.fk_user_non_confirmed.email,
        )
        user.set_password(modal_code.fk_user_non_confirmed.password)
        user.save()

        return Response(status=status.HTTP_204_NO_CONTENT)


    @extend_schema(
        request=user_serializers.UserNonCofirmedSerializer,
        responses={204: OpenApiTypes.NONE, 400: ErrorSerializer}
    )
    def post(self, request: Request) -> Response:
        mail_code = ''.join(str(randint(0, 9)) for _ in range(8))

        user_non_confirmed_serialized = user_serializers.UserNonCofirmedSerializer(data=request.data)
        user_non_confirmed_serialized.is_valid(raise_exception=True)

        user_non_confirmed_model = user_non_confirmed_serialized.save()

        model_code = user_models.CodeModel.objects.create(
            fk_user_non_confirmed=user_non_confirmed_model,
            email_code=mail_code
        )

        html_render = user_html_template.HtmlTemplate(
            user_html_template.html_template,
            user_html_template.basic_html_template,
            {
                'codigo_confirmacao': model_code.email_code,
                'link_confirmacao': f"{reverse("user_code", request=request)}?{urlencode({'code': model_code.email_code})}"
            }
        )

        send_mail(
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=["ogirdo.sant@gmail.com"],
            subject="Teste de E-mail com HTML",
            message=html_render.basic_render(),
            html_message=html_render.render(),
            fail_silently=False,
        )
        return Response(status=status.HTTP_204_NO_CONTENT)
