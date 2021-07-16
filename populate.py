from escala_de_folga.apps.cadastros.models import *
from faker import Faker
from django.contrib.auth.models import User

user = User.objects.create_user('caio', password='1q2w')
user.is_superuser = True
user.is_staff = True
user.save()

faker: Faker = Faker(locale='pt-br')

for i in range(10):
    Medico(nome=faker.first_name(), sobrenome=faker.last_name(
    ), admissao=faker.past_date('-300d'), preferencia=faker.random_int(0, 5)).save()
for i in range(6):
    Posto(nome="Unidade "+faker.neighborhood(),
          endereco=faker.address()).save()
