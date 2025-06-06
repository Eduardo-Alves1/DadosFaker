import requests

from faker import Faker


faker = Faker("pt_BR")


def generate_car():
    return {
        "chassi": faker.vin(),
        # "modelo": faker.word(),
        "ano": faker.year(),
        # "cor": faker.color_name(),
        "placa": faker.license_plate(),
        "quilometragem": faker.random_int(min=0, max=300000),
    }
