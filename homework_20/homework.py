"""
Створення моделі даних: Створіть просту модель даних для системи управління студентами.
Модель може містити таблиці для студентів, курсів та їх відношень.
Кожен студент може бути зареєстрований на декілька курсів.
Наприклад, створити 5 курсів, та розподілити рандомно 20 студентів.
Виконання базових операцій: Напишіть програму, яка додає нового студента до бази даних та додає його до певного курсу.
Переконайтеся, що ці зміни коректно відображаються у базі даних.
Запити до бази даних: Напишіть запити до бази даних, які повертають інформацію про студентів,
зареєстрованих на певний курс, або курси, на які зареєстрований певний студент.
Оновлення та видалення даних: Реалізуйте можливість оновлення даних про студентів або курси,
а також видалення студентів з бази даних.
"""

import os
import random

from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

from homework_20.declarative_base import Base
from homework_20.table_models.table_students import Student
from homework_20.table_models.table_courses import Course
from homework_20.data_provider import get_student

from homework_20.helpers_service import (
    update_student_name,
    update_course_name,
    delete_student_by_id,
    get_courses_by_student_name,
    get_students_by_course_name,
    delete_course_by_id,
)

load_dotenv()


class SQLAlchemyClient:

    def __init__(self):
        self.db_url = os.getenv("POSTGRES_DB_URL")
        self.__engine: Engine = create_engine(self.db_url)
        self.__session = self.__create_session()

    @property
    def session(self):
        return self.__session

    @property
    def engine(self):
        return self.__engine

    def __create_session(self):
        session = sessionmaker(bind=self.engine)
        return session()

    def create_table(self, table_model):
        table_model.metadata.create_all(self.engine)

    def create_all_tables(self):
        Base.metadata.create_all(self.engine)

    def close_connection(self):
        self.session.close()


if __name__ == "__main__":

    sqlalchemy_client = SQLAlchemyClient()
    sqlalchemy_client.create_all_tables()
    session = sqlalchemy_client.session

    # наповнюємо таблиці

    course_1 = Course(name="Computer Science")
    course_2 = Course(name="Mathematics")
    course_3 = Course(name="Economics")
    course_4 = Course(name="History")
    course_5 = Course(name="Physics")
    session.add_all([course_1, course_2, course_3, course_4, course_5])
    sqlalchemy_client.session.commit()

    all_courses = session.query(Course).all()
    for _ in range(20):
        random_courses = random.sample(all_courses, 3)
        new_student: Student = get_student()
        for random_course in random_courses:
            new_student.courses.append(random_course)
        session.add(new_student)
    sqlalchemy_client.session.commit()

    # оновлюємо і видаляємо дані з таблиці

    update_student_name(session, 1, "Test User")
    update_course_name(session, 1, "Test Course")
    delete_student_by_id(session, 2)
    delete_course_by_id(session, 2)
    sqlalchemy_client.session.commit()

    # збираємо інформацію студент-курси, курс-студенти

    history_course_students = get_students_by_course_name(session, "Physics")
    if history_course_students:
        print(f"\nStudents registered on course 'History':")
        for student in history_course_students:
            print(f" - [Student ID: {student.id}] | Student Name: {student.name}")

    student_name = ""
    student_courses = get_courses_by_student_name(session, student_name)
    if student_courses:
        courses_list = [course.name for course in student_courses]
        print(
            f"\nStudent {student_name} registered on following courses: {courses_list}"
        )

    session.close()
    sqlalchemy_client.close_connection()
