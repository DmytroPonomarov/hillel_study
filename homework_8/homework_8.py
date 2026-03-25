class Student:

    def __init__(self, name, second_name, age, average_grade):
        self.name = name
        self.second_name = second_name
        self.age = age
        self.average_grade = average_grade

    def new_grade(self, new_value):
        self.average_grade = new_value

    def print_student_info(self):
        print(f"Name: {self.name} {self.second_name}")
        print(f"Age: {self.age}")
        print(f"Average grade: {self.average_grade}")


student_1 = Student("Dmytro", "Ponomarov", 20, 0)
student_1.new_grade(30)
student_1.print_student_info()


# Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал".
# Створіть об'єкт цього класу, представляючи студента.
# Потім додайте метод до класу "Студент",
# який дозволяє змінювати середній бал студента. Виведіть інформацію про студента та змініть його середній бал.
