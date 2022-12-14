from tests.data.data import Person
from faker import Faker

faker_en = Faker('en-US')
Faker.seed()

def generation_user():
    yield Person (
        first_name = faker_en.first_name(),
        last_name = faker_en.last_name(),
        email = faker_en.email(),
        telepfone = faker_en.phone_number(),
        password =faker_en.password()
    )
