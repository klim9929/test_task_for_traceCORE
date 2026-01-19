from dataclasses import dataclass, asdict
import faker


@dataclass
class UserData:
    def __init__(self):
        self.faker = faker.Faker()

    @property
    def data(self):
        return {
            "id": self.faker.random_number(digits=5),
            "username": self.faker.user_name(),
            "firstName": self.faker.first_name(),
            "lastName": self.faker.last_name(),
            "email": self.faker.email(),
            "password": self.faker.password(),
            "phone": self.faker.phone_number(),
            "userStatus": self.faker.random_element(elements=(0, 1, 2))
        }


