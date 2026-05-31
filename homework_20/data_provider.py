from faker import Faker
from homework_20.table_models.table_students import Student

fake = Faker()


def get_student() -> Student:
    return Student(name=fake.name())
