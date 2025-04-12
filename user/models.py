from django.db import models

class UserNonConfirmed(models.Model):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=128)

class CodeModel(models.Model):
    # Vai ser enviado para o email cadastrado por fator de segurança
    email_code = models.CharField(max_length=8)
    # O usuário vai ter um tempo limite para cadastrar esse token
    created_at = models.DateTimeField(auto_now_add=True)
    # Para evitar que um token seja usado duas vezes
    used = models.BooleanField(default=False)

    fk_user_non_confirmed = models.ForeignKey(UserNonConfirmed, on_delete=models.CASCADE)

