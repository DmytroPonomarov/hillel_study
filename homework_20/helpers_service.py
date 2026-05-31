from homework_20.table_models.table_students import Student
from homework_20.table_models.table_courses import Course


def update_student_name(session, student_id: int, new_name: str):
    student = session.query(Student).filter_by(id=student_id).first()
    if student:
        student.name = new_name
        session.commit()
        print(f"Student with id {student_id} renamed to {new_name}")
        return True
    print(f"Student with {student_id} not found")
    return False


def update_course_name(session, course_id: int, new_name: str):
    course = session.query(Course).filter_by(id=course_id).first()
    if course:
        course.name = new_name
        session.commit()
        print(f"Course with id {course_id} renamed to {new_name}")
        return True
    print(f"Course with ID {course_id} not found!")
    return False


def delete_student_by_id(session, student_id: int):
    student = session.query(Student).filter_by(id=student_id).first()
    if student:
        session.delete(student)
        session.commit()
        print(f"Student {student.name} with ID {student_id}) is deleted.")
        return True
    print(f"Student with ID {student_id} not found")
    return False


def delete_course_by_id(session, course_id: int):
    course = session.query(Course).filter_by(id=course_id).first()
    if course:
        session.delete(course)
        session.commit()
        print(f"Course {course.name} with ID {course_id} is deleted.")
        return True
    print(f"Course with ID {course_id} not found")
    return False


def get_courses_by_student_name(session, student_name: str):
    student = session.query(Student).filter_by(name=student_name).first()
    if not student:
        print(f"Student with name {student_name} not found")
        return False
    return student.courses


def get_students_by_course_name(session, course_name: str):
    course = session.query(Course).filter_by(name=course_name).first()
    if not course:
        print(f"Course with name {course_name} not found")
        return False
    return course.students
