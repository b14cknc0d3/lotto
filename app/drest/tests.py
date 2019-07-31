# from django.utils.http import urlencode
# from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from .models import Lno
# from . import views


class LnoTestCase(APITestCase):

    def CreateUserAndGetToken(self):
        user = User.objects.create_user('user01', 'user01@example.com', 'user01P4ssw0rD')
        token = Token.objects.create(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token {0}'.format(token.key))

    def TestPostWithoutToken(self):
        new_lno_lno = '123456'
        new_lno_phone = '22222'
        new_lno_address = 'addsdsf'
        response = self.post_lno(
            new_lno_lno,
            new_lno_address,
            new_lno_phone
        )
        print(response)
        print(Lno.objects.count())
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert Lno.objects.count() == 0
