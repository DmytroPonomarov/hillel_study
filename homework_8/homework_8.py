class Student:
    name = "Dmytro"
    second_name = "Ponomarov"
    age = 20
    average_grade = 0

    def new_grade(self, new_value):
        self.average_grade = new_value


student: Student = Student()

student.new_grade(30)

print(
    f"Student: {student.name} {student.second_name}"
    f"\nAge: {student.age}"
    f"\nAverage grade: {student.average_grade}"
)

# Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал".
# Створіть об'єкт цього класу, представляючи студента.
# Потім додайте метод до класу "Студент",
# який дозволяє змінювати середній бал студента. Виведіть інформацію про студента та змініть його середній бал.
