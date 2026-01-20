import faker
from dataclasses import dataclass, asdict

"""Фабрика генерации пользователей через faker."""

@dataclass
class UserData:
    id: int
    username: str
    firstName: str
    lastName: str
    email: str
    password: str
    phone: str
    userStatus: int

    def __init__(self):
        fake = faker.Faker()
        self.id = fake.random_number(digits=5)
        self.username = fake.user_name()
        self.firstName = fake.first_name()
        self.lastName = fake.last_name()
        self.email = fake.email()
        self.password = fake.password()
        self.phone = fake.phone_number()
        self.userStatus = fake.random_element(elements=(0, 1, 2))

    def as_dict(self):
        """Преобразует объект в словарь для отправки в API."""
        return asdict(self)