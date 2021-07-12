from escala_de_folga.apps.cadastros.models import *
from faker import Faker

faker = Faker(locale='pt-br')

for i in range(10):
    nome, sobrenome = faker.name().split()[:2]
    Medico(nome=nome, sobrenome=sobrenome, admissao=faker.past_date('-300d'), folga=faker.random_int(0, 5)).save()
